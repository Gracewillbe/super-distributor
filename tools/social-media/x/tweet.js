#!/usr/bin/env node

import crypto from 'crypto';
import https from 'https';
import { HttpsProxyAgent } from 'https-proxy-agent';
import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';

const __dirname = path.dirname(fileURLToPath(import.meta.url));

// Load credentials from .env file or environment variables
function loadConfig() {
  const envPath = path.join(__dirname, '.env');

  if (fs.existsSync(envPath)) {
    const envContent = fs.readFileSync(envPath, 'utf-8');
    envContent.split('\n').forEach(line => {
      const match = line.match(/^([^#=]+)=(.*)$/);
      if (match) {
        const key = match[1].trim();
        const value = match[2].trim();
        if (!process.env[key]) {
          process.env[key] = value;
        }
      }
    });
  }

  const config = {
    consumerKey: process.env.TWITTER_API_KEY,
    consumerSecret: process.env.TWITTER_API_SECRET,
    accessToken: process.env.TWITTER_ACCESS_TOKEN,
    accessSecret: process.env.TWITTER_ACCESS_SECRET,
  };

  // Validate credentials
  const missing = Object.keys(config).filter(key => !config[key]);
  if (missing.length > 0) {
    console.error('❌ Missing credentials:', missing.join(', '));
    console.error('\nPlease create a .env file or set environment variables.');
    console.error('See .env.example for template.');
    process.exit(1);
  }

  return config;
}

function percentEncode(str) {
  return encodeURIComponent(str).replace(/[!'()*]/g, (c) =>
    `%${c.charCodeAt(0).toString(16).toUpperCase()}`
  );
}

function generateOAuthSignature(method, url, params, consumerSecret, tokenSecret = '') {
  const sortedParams = Object.keys(params)
    .sort()
    .map(key => `${percentEncode(key)}=${percentEncode(params[key])}`)
    .join('&');

  const signatureBase = `${method.toUpperCase()}&${percentEncode(url)}&${percentEncode(sortedParams)}`;
  const signingKey = `${percentEncode(consumerSecret)}&${percentEncode(tokenSecret)}`;

  return crypto.createHmac('sha1', signingKey).update(signatureBase).digest('base64');
}

async function postTweet(text, config, options = {}) {
  const url = 'https://api.x.com/2/tweets';
  const method = 'POST';

  const oauthParams = {
    oauth_consumer_key: config.consumerKey,
    oauth_token: config.accessToken,
    oauth_signature_method: 'HMAC-SHA1',
    oauth_timestamp: Math.floor(Date.now() / 1000).toString(),
    oauth_nonce: crypto.randomBytes(16).toString('hex'),
    oauth_version: '1.0',
  };

  const signature = generateOAuthSignature(
    method,
    url,
    oauthParams,
    config.consumerSecret,
    config.accessSecret
  );
  oauthParams.oauth_signature = signature;

  const authHeader = 'OAuth ' + Object.keys(oauthParams)
    .sort()
    .map(key => `${percentEncode(key)}="${percentEncode(oauthParams[key])}"`)
    .join(', ');

  const body = JSON.stringify({ text });

  const requestOptions = {
    method,
    hostname: 'api.x.com',
    path: '/2/tweets',
    headers: {
      'Authorization': authHeader,
      'Content-Type': 'application/json',
      'Content-Length': Buffer.byteLength(body),
    },
  };

  // Use proxy if configured
  const proxy = process.env.https_proxy || process.env.HTTPS_PROXY;
  if (proxy) {
    requestOptions.agent = new HttpsProxyAgent(proxy);
    if (options.verbose) {
      console.log('Using proxy:', proxy);
    }
  }

  return new Promise((resolve, reject) => {
    const req = https.request(requestOptions, (res) => {
      let data = '';
      res.on('data', chunk => data += chunk);
      res.on('end', () => {
        if (res.statusCode === 201) {
          const result = JSON.parse(data);
          resolve(result);
        } else {
          reject(new Error(`HTTP ${res.statusCode}: ${data}`));
        }
      });
    });

    req.on('error', reject);
    req.setTimeout(20000, () => {
      req.destroy();
      reject(new Error('Request timeout'));
    });

    req.write(body);
    req.end();
  });
}

// Parse command line arguments
function parseArgs(args) {
  const options = {
    preview: false,
    verbose: false,
  };

  const textParts = [];

  for (let i = 0; i < args.length; i++) {
    const arg = args[i];

    if (arg === '--preview' || arg === '-p') {
      options.preview = true;
    } else if (arg === '--verbose' || arg === '-v') {
      options.verbose = true;
    } else if (arg === '--help' || arg === '-h') {
      options.showHelp = true;
    } else {
      textParts.push(arg);
    }
  }

  options.text = textParts.join(' ');
  return options;
}

function showHelp() {
  console.log(`
X Auto-Posting Tool

Usage:
  node tweet.js "Your tweet text"
  node tweet.js "Your tweet" --preview

Options:
  -p, --preview    Preview tweet without posting
  -v, --verbose    Show detailed output
  -h, --help       Show this help message

Examples:
  node tweet.js "Hello, world! 🚀"
  node tweet.js "Check out my new blog post" --preview

Configuration:
  Create a .env file with your X API credentials.
  See .env.example for template.

More info:
  https://github.com/Gracewillbe/super-distributor/tree/main/tools/twitter
`);
}

// Main
async function main() {
  const args = process.argv.slice(2);
  const options = parseArgs(args);

  if (options.showHelp || args.length === 0) {
    showHelp();
    process.exit(0);
  }

  const text = options.text;

  if (!text) {
    console.error('❌ No tweet text provided');
    console.error('Usage: node tweet.js "Your tweet text"');
    process.exit(1);
  }

  if (text.length > 280) {
    console.error(`❌ Tweet too long: ${text.length} characters (max 280)`);
    process.exit(1);
  }

  console.log('📝 Tweet content:');
  console.log('─'.repeat(50));
  console.log(text);
  console.log('─'.repeat(50));
  console.log(`Length: ${text.length} characters\n`);

  if (options.preview) {
    console.log('👁️  Preview mode - not posting');
    process.exit(0);
  }

  try {
    const config = loadConfig();
    console.log('🚀 Posting to X...\n');

    const result = await postTweet(text, config, options);

    console.log('✅ Tweet posted successfully!');
    console.log('Tweet ID:', result.data.id);
    console.log('URL: https://x.com/user/status/' + result.data.id);

  } catch (error) {
    console.error('\n❌ Failed to post tweet');
    console.error('Error:', error.message);

    if (error.message.includes('403')) {
      console.error('\n💡 Troubleshooting:');
      console.error('1. Check if your X app is configured as "Web App, Automated App or Bot"');
      console.error('2. Verify API credentials are correct');
      console.error('3. Ensure you have credits in your X account (pay-per-use)');
      console.error('4. See README.md for detailed setup instructions');
    }

    process.exit(1);
  }
}

main();
