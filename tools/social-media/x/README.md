# X Auto-Posting System

**Complete automation for social media posting - replace your social media manager.**

This tool handles the entire X posting workflow: content optimization, formatting, image handling, hashtags, and automated publishing.

---

## What This Does

✅ **Content Optimization** - Formats tweets for maximum engagement
✅ **Character Management** - Auto-splits long content into threads
✅ **Image Handling** - Attaches images with alt text
✅ **Hashtag Strategy** - Adds relevant hashtags without spam
✅ **Automated Publishing** - Posts directly to X
✅ **Preview Mode** - Review before posting

---

## Setup Guide

### Step 1: Get X API Access

#### 1.1 Create a X Developer Account
1. Go to [X Developer Portal](https://developer.twitter.com/en/portal/dashboard)
2. Sign up with your X account
3. Create a new Project and App

#### 1.2 Configure App Settings
1. In your App settings, go to **"User authentication settings"**
2. Click **"Set up"**
3. Choose **"Web App, Automated App or Bot"**
4. Fill in:
   - **App permissions**: `Read and Write`
   - **Callback URI**: `http://127.0.0.1` (required but not used)
   - **Website URL**: `https://example.com` (or your actual site)
5. Click **"Save"**

#### 1.3 Get API Keys
1. Go to **"Keys and tokens"** tab
2. Copy these 4 credentials:
   - **API Key** (Consumer Key)
   - **API Key Secret** (Consumer Secret)
   - **Access Token**
   - **Access Token Secret**

#### 1.4 Handle Billing (Pay-per-use)
- X API requires payment for posting
- Go to **Billing** → **Buy Credits**
- Add $5 (enough for ~2500 tweets)
- Cost: ~$0.002 per tweet

---

### Step 2: Configure the Tool

#### 2.1 Install Dependencies
```bash
cd /Users/grace/coding-projects/super-distributor/tools/twitter
npm install
```

#### 2.2 Set Up Credentials
Create `.env` file:
```bash
TWITTER_API_KEY=your_api_key
TWITTER_API_SECRET=your_api_secret
TWITTER_ACCESS_TOKEN=your_access_token
TWITTER_ACCESS_SECRET=your_access_secret
```

**Security Note:** Never commit `.env` to git. Add to `.gitignore`.

---

### Step 3: Test the Setup

```bash
node tweet.js "Hello, world! 🚀"
```

If successful, you'll see:
```
✅ Tweet posted successfully!
Tweet ID: 1234567890
URL: https://x.com/user/status/1234567890
```

---

## Usage

### Basic Tweet
```bash
node tweet.js "Your tweet content here"
```

### Tweet with Hashtags
```bash
node tweet.js "Launching our new feature! #ProductLaunch #SaaS #IndieHackers"
```

### Tweet Thread (Auto-split)
```bash
node tweet.js --thread "Long content that will be automatically split into multiple tweets. Each tweet stays under 280 characters. The tool handles threading automatically."
```

### Tweet with Image
```bash
node tweet.js "Check out our new design!" --image ./path/to/image.png --alt "Product screenshot"
```

### Preview Mode (Don't Post)
```bash
node tweet.js "Draft tweet" --preview
```

---

## Best Practices

### Content Optimization

#### Character Limits
- **Standard tweet**: 280 characters max
- **With link**: Leave 23 chars for URL shortening
- **With image**: Same as standard (image doesn't count)

#### Engagement Tips
1. **Hook in first line** - Grab attention immediately
2. **Clear value prop** - What's in it for the reader?
3. **Call to action** - Tell them what to do next
4. **Visual elements** - Use emoji sparingly (1-2 per tweet)

#### Thread Strategy
```
Thread structure:
1️⃣ Hook - Problem or bold statement
2️⃣ Context - Why this matters
3️⃣ Solution - Your main points (3-5 tweets)
4️⃣ Proof - Data, examples, testimonials
5️⃣ CTA - Link, ask, or next step
```

### Hashtag Strategy

#### How Many?
- **1-2 hashtags** = Best engagement
- **3+ hashtags** = Looks spammy, reduces reach

#### Which Ones?
- **Niche-specific** (e.g., #IndieHackers for builders)
- **Medium volume** (10K-100K tweets, not millions)
- **Relevant** (actually describes your content)

### Image Guidelines

#### Specs
- **Format**: PNG or JPG
- **Size**: 1200x675px (16:9 ratio) for best display
- **File size**: Under 5MB
- **Alt text**: Always add for accessibility

#### What Works
- Screenshots with highlights
- Simple graphics (not text-heavy)
- Behind-the-scenes photos
- Data visualizations

### Timing

#### Best Times to Post (US audience)
- **Weekdays**: 9-11am ET, 12-1pm ET, 5-6pm ET
- **Weekends**: 9am-11am ET

#### Frequency
- **Minimum**: 3-5 tweets/week
- **Optimal**: 1-2 tweets/day
- **Maximum**: 5 tweets/day (avoid spam)

---

## Advanced Features

### Scheduled Posting
```bash
# Post at specific time
node tweet.js "Scheduled tweet" --schedule "2026-04-10 09:00"
```

### Analytics Tracking
```bash
# Add UTM parameters to links
node tweet.js "Check this out: https://yoursite.com" --utm campaign=twitter_april
```

### A/B Testing
```bash
# Test two versions
node tweet.js "Version A: Clear and direct" --test-id test1
node tweet.js "Version B: Creative and fun" --test-id test1
```

---

## Troubleshooting

### Common Errors

#### "Authentication failed"
- **Cause**: Wrong API credentials
- **Fix**: Regenerate keys in Developer Portal, update `.env`

#### "Forbidden - oauth1 permissions"
- **Cause**: App not configured for posting
- **Fix**: Set app type to "Web App, Automated App or Bot"

#### "Credit balance insufficient"
- **Cause**: No credits in pay-per-use account
- **Fix**: Add credits in Billing section

#### "Request timeout"
- **Cause**: Network/proxy issues
- **Fix**: Check proxy settings in environment variables

### Proxy Configuration

If behind a proxy:
```bash
export https_proxy=http://127.0.0.1:10887
export http_proxy=http://127.0.0.1:10887
```

---

## Integration with Claude Code

### MCP Server Setup (Optional)

For Claude Code integration, configure MCP in `.mcp.json`:

```json
{
  "mcpServers": {
    "twitter-automation": {
      "command": "node",
      "args": ["/path/to/super-distributor/tools/twitter/mcp-server.js"],
      "env": {
        "TWITTER_API_KEY": "your_key",
        "TWITTER_API_SECRET": "your_secret",
        "TWITTER_ACCESS_TOKEN": "your_token",
        "TWITTER_ACCESS_TOKEN_SECRET": "your_token_secret"
      }
    }
  }
}
```

Then use in Claude Code:
```
Claude, post to X: "My tweet content"
```

---

## Workflow Examples

### Daily Social Media Manager Workflow

```bash
# Morning: Share insight
node tweet.js "Just learned: [insight]. Game changer for [audience]. 💡"

# Midday: Promote content
node tweet.js "New blog post: [title]\n\n[2-sentence summary]\n\n[link] #YourNiche" --image feature.png

# Evening: Engage
node tweet.js "What's the biggest challenge you're facing with [topic]? 🤔"
```

### Product Launch Workflow

```bash
# Day before: Tease
node tweet.js "Launching something new tomorrow. Been working on this for months. 🚀"

# Launch day: Announce
node tweet.js --thread "Excited to launch [Product]! 🎉\n\n[Problem it solves]\n[How it works]\n[Who it's for]\n[Link to try it]\n\nRetweet if you think this is useful! 🙏"

# Follow-up: Social proof
node tweet.js "Just hit 100 users in 24 hours! 🎊\n\nThank you all for the support. [Screenshot]" --image stats.png
```

---

## Cost Analysis

### Typical Usage
- **Daily posting** (2 tweets/day): ~$0.12/month
- **Active campaign** (10 tweets/day): ~$0.60/month
- **Heavy user** (50 tweets/day): ~$3/month

**Bottom line**: $5 credit lasts 3-6 months for most indie makers.

---

## Files in This Tool

```
twitter/
├── README.md              # This file
├── tweet.js               # Main posting script
├── mcp-server.js          # MCP integration (optional)
├── package.json           # Dependencies
├── .env.example           # Credentials template
└── utils/
    ├── format.js          # Text formatting
    ├── thread.js          # Thread splitting
    ├── image.js           # Image handling
    └── analytics.js       # Performance tracking
```

---

## Next Steps

1. ✅ Complete API setup
2. ✅ Test basic posting
3. 📝 Create content calendar
4. 🤖 Automate daily posts
5. 📊 Track engagement
6. 🔄 Optimize based on data

---

## Support

**Issues?** Open an issue in the [super-distributor repo](https://github.com/Gracewillbe/super-distributor/issues)

**Questions?** Tag [@YourXHandle](https://x.com/yourusername)

---

*Part of [Super Distributor](https://github.com/Gracewillbe/super-distributor) - Open-source growth tools for indie makers.*
