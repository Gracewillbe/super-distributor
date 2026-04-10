---
name: landing-page-builder
description: Generate a complete, conversion-focused HTML landing page from your messaging - ready to deploy in minutes
---

# Landing Page Builder

Turn your messaging into a beautiful, converting landing page.

Based on **Chapter 05 - Landing Page** from Super Distributor playbooks.

---

## What This Skill Does

Takes your messaging and generates a **complete, single-file HTML landing page**:
- ✅ **5-section or 7-section structure** (Hero → Problem → Solution → How It Works → CTA)
- ✅ **Grace's design aesthetic** (Japanese modern, restrained, clean typography)
- ✅ **Zero dependencies** - single HTML file with inline CSS
- ✅ **Mobile-responsive** - works on all devices
- ✅ **Ready to deploy** - to Vercel, Netlify, or any static host

---

## Step 1: Choose Your Structure

**Option A: 5-Section Page** (Recommended for most indie products)
- Hero
- Problem
- Solution
- How It Works (optional)
- CTA

**Option B: 7-Section Page** (For complex products needing more proof)
- All of the above, plus:
- Features Deep Dive
- Social Proof / Testimonials
- FAQ

**Which structure do you want?** (Type "5" or "7")

---

## Step 2: Provide Your Messaging

You can either:
- **Use messaging-generator output** (if you just ran that skill)
- **Provide messaging manually** (I'll ask you questions)

**Do you have messaging ready from messaging-generator?** (Yes/No)

---

## Step 3A: If You Have Messaging Ready

Provide these from your messaging-generator output:

1. **One-liner** (10-second pitch)
2. **Value proposition** (30-second version, 3 sentences)
3. **Core message pillars** (3-5 pillars)

---

## Step 3B: If You're Providing Messaging Manually

I'll ask you these questions:

**Question 1: Headline (Hero)**
- What's the main outcome users get?
- Format: "[Outcome] for [Who]" or "[Outcome] without [Pain]"
- Example: "Ship from zero to your first users"

**Question 2: Subheadline (Hero)**
- How do you deliver that outcome?
- One sentence, plain language
- Example: "Open-source playbooks and tools for indie makers"

**Question 3: Problem Statement**
- What pain point are you solving?
- 2-3 sentences, use their words
- Make them feel seen

**Question 4: Solution Statement**
- How does your product solve the problem?
- 1-2 sentences

**Question 5: Key Benefits**
- What are 3-5 outcomes users get?
- Use bullets, start with verbs
- Focus on outcomes, not features

**Question 6: Call-to-Action**
- What action do you want visitors to take?
- Examples: "Start Free Trial", "Download Now", "Join Waitlist", "Browse Playbooks"

**Question 7: CTA Link**
- Where should the button go?
- URL or GitHub repo link

**Question 8: How It Works (Optional)**
- Can you explain your product in 3 simple steps?
- If yes, provide the 3 steps. If no, we'll skip this section.

---

## Step 4: Design Preferences

**Color Scheme:**
- **Option 1:** Japanese Modern (Black #181818 + Warm White #FAFAF8 + Amber Gold accent #C49A5C) — **Recommended**
- **Option 2:** Minimalist B&W (Pure black + Pure white + Blue accent)
- **Option 3:** Custom (you provide 3 colors: primary, secondary, accent)

**Which color scheme?** (Type "1", "2", or "3")

---

## Step 5: Optional Sections (For 7-Section Version)

**If you chose 7-section structure, provide:**

### Features Deep Dive (Optional)
- 3-6 feature cards
- Each with: Icon emoji + Headline + 1-sentence description

### Social Proof (Optional)
- Testimonials (with real names)
- Usage stats ("Trusted by 10,000+ makers")
- Media mentions ("Featured on Product Hunt, HN")

### FAQ (Optional)
- Top 3-5 questions that stop people from converting
- Format: Question → Short answer

**If you don't have these yet, we'll skip them.**

---

## Step 6: Generate Your Landing Page

Based on your inputs, I'll generate a complete HTML file with:

### Design System
- **Typography:**
  - Headlines: DM Serif Display (serif, elegant, no bold needed)
  - Body: Inter (sans-serif, readable)
  - Loaded from Google Fonts

- **Layout:**
  - Max-width container (720px for readability)
  - Generous white space and padding
  - Clean section dividers
  - Non-symmetric hero layout

- **Components:**
  - Bold, high-contrast CTA buttons (square corners, not rounded)
  - Mobile-first responsive design
  - Fast loading (no external dependencies except fonts)
  - SEO-friendly semantic HTML

### Page Structure

```html
<!DOCTYPE html>
<html>
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>[Your Product Name]</title>
  <meta name="description" content="[Your one-liner]">
  [Inline CSS]
</head>
<body>
  <!-- Hero -->
  <!-- Problem -->
  <!-- Solution -->
  <!-- How It Works (if included) -->
  <!-- Features (if 7-section) -->
  <!-- Social Proof (if 7-section) -->
  <!-- FAQ (if 7-section) -->
  <!-- CTA -->
  <!-- Footer -->
</body>
</html>
```

---

## Step 7: Download and Deploy

Your landing page will be saved as `landing-page.html`.

### Deploy Options:

**Option 1: Vercel (Easiest)**
```bash
# Install Vercel CLI
npm i -g vercel

# Deploy
vercel landing-page.html
```

**Option 2: Netlify Drop**
- Go to https://app.netlify.com/drop
- Drag and drop `landing-page.html`
- Done

**Option 3: GitHub Pages**
- Rename to `index.html`
- Push to a repo
- Enable GitHub Pages in settings

**Option 4: Any Static Host**
- Upload to your server
- Works anywhere that serves HTML

---

## Design Principles Applied

Based on Chapter 05 and Grace's design aesthetic:

### Copywriting
- ✅ Clarity over cleverness
- ✅ Outcomes over features
- ✅ "You" language, not "we" language
- ✅ Active voice
- ✅ Specific, not vague

### Visual Design
- ✅ Limited color palette (1 primary + 1-2 neutrals + 1 accent)
- ✅ Good typography (2 fonts: serif for headlines, sans for body)
- ✅ Generous white space
- ✅ No stock photos, no fake testimonials
- ✅ Fast loading, mobile-responsive

### Conversion Optimization
- ✅ 5-second test optimized (value clear immediately)
- ✅ CTA above the fold and at bottom
- ✅ Removed all friction ("No signup required", etc.)
- ✅ Single-purpose focus (one clear action)

---

## The 5-Second Test

After I generate your page, test it:

1. Show it to someone who's never seen it
2. Give them 5 seconds
3. Take it away
4. Ask: "What does this product do? Who is it for?"

**If they can't answer, we'll iterate on the hero section.**

---

## Conversion Rate Benchmarks

What to expect:
- **Great:** 10%+ (waitlist or free tool)
- **Good:** 3-5% (sign-up or trial)
- **Average:** 1-2% (paid product, cold traffic)
- **Bad:** <1%

**If you're under 1%, let's fix the copy or targeting.**

---

## What Comes Next

After you deploy your landing page:

1. **Add analytics** - Plausible, Fathom, or Google Analytics
2. **Drive traffic** - Use Chapter 06 (Social Media) and Chapter 07 (Launch Day)
3. **Iterate based on data** - Track what works, improve what doesn't

**Related skills:**
- `messaging-generator` - Create messaging before building the page
- `launch-planner` - Plan your launch once the page is live

---

## Need Help?

- **Stuck on messaging?** Use the `messaging-generator` skill first
- **Want to see examples?** Check out Chapter 05 - Landing Page playbook
- **Ready to launch?** Use the `launch-planner` skill

**Your landing page is a conversion system, not an art project. Let's ship something that works.**
