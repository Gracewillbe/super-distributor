## Landing Page Builder

**Claude Code skill for Super Distributor**

Generate a complete, conversion-focused landing page in minutes.

---

## What It Does

This skill turns your messaging into a **ready-to-deploy HTML landing page**.

**You provide:**
- Your messaging (from messaging-generator or manually)
- Design preferences
- Optional content (features, social proof, FAQ)

**You get:**
- Complete single-file HTML landing page
- Grace's design aesthetic (Japanese modern, clean, professional)
- Mobile-responsive, fast-loading
- Ready to deploy to Vercel, Netlify, GitHub Pages, or any static host

---

## How to Use

### In Claude Code

```
Use the landing-page-builder skill
```

The skill will guide you through:
1. Choose structure (5-section or 7-section)
2. Provide messaging
3. Select design preferences
4. Add optional sections
5. Generate HTML file
6. Deploy

---

## What You'll Get

### A Complete Landing Page With:

**5-Section Structure (Default):**
1. **Hero** - Headline, subheadline, CTA, visual
2. **Problem** - Pain point validation
3. **Solution** - How you solve it + key benefits
4. **How It Works** - 3-step process (optional)
5. **CTA** - Final call-to-action + reassurance

**7-Section Structure (For Complex Products):**
- All of the above, plus:
- **Features Deep Dive** - Detailed feature cards
- **Social Proof** - Testimonials, stats, media mentions
- **FAQ** - Answer common objections

---

### Design System

**Typography:**
- Headlines: DM Serif Display (serif, elegant)
- Body: Inter (sans-serif, clean)

**Colors (Japanese Modern - Default):**
- Primary: #181818 (near-black)
- Secondary: #FAFAF8 (warm white)
- Accent: #C49A5C (amber gold)

**Layout:**
- Max-width container for readability
- Generous white space
- Non-symmetric hero
- Square buttons (no rounded corners)
- Mobile-first responsive

---

## Prerequisites

**You should have:**
- ✅ Your messaging ready (use `messaging-generator` skill first)
- ✅ CTA decision (what action do visitors take?)
- ✅ CTA link (where does the button go?)

**Optional but helpful:**
- Screenshots or visuals
- Testimonials or social proof
- FAQ content

---

## Tips for Best Results

### Copywriting
1. **Hero headline** - One clear outcome, not a clever phrase
2. **Problem section** - Use your users' exact words
3. **Solution bullets** - Lead with outcomes, not features
4. **CTA copy** - Be specific ("Browse Playbooks" > "Get Started")

### Design
1. **Stick with default colors** unless you have strong preferences
2. **Use real screenshots** over mockups or stock photos
3. **Keep it simple** - More content ≠ better conversion
4. **Test on mobile** - Most traffic will be mobile

### Conversion
1. **Run the 5-second test** - Show to 3 people, ask what it does
2. **Remove friction** - Add reassurance near CTA ("Free", "No signup")
3. **One clear action** - Don't give visitors too many choices

---

## Common Mistakes to Avoid

❌ **Starting with design** - Write copy first, design last
❌ **Feature soup** - Nobody cares about your features list
❌ **Talking to everyone** - Pick one specific user
❌ **Weak CTA** - "Learn More" is not a call-to-action
❌ **Over-designing** - Simple converts better than fancy

---

## After You Deploy

### 1. Add Analytics
- Plausible (privacy-focused)
- Fathom (simple)
- Google Analytics (comprehensive)

### 2. Drive Traffic
- Use Chapter 06 - Social Media
- Use `launch-planner` skill for launch content

### 3. Track Conversion Rate
- **Great:** 10%+ (waitlist/free tool)
- **Good:** 3-5% (signup/trial)
- **Average:** 1-2% (paid product)
- **Bad:** <1% → Fix your copy

### 4. Iterate
- Test headlines
- Try different CTAs
- Add or remove sections based on data

---

## Deploy Options

**Vercel (Recommended - Fastest)**
```bash
npm i -g vercel
vercel landing-page.html
```

**Netlify Drop (No CLI)**
- https://app.netlify.com/drop
- Drag and drop your HTML file

**GitHub Pages (Free)**
- Rename to `index.html`
- Push to repo, enable Pages in settings

**Any Static Host**
- Upload HTML file
- Works anywhere

---

## Related Resources

- **Playbook:** [Chapter 05 - Landing Page](../../playbook/05-landing-page.md)
- **Previous:** [Chapter 04 - Messaging](../../playbook/04-messaging.md)
- **Next:** [Chapter 06 - Social Media](../../playbook/06-social-media.md)

**Related Skills:**
- `messaging-generator` - Create messaging first
- `launch-planner` - Plan your launch
- `seo-optimizer` - Optimize SEO after shipping (coming soon)

---

## Design Philosophy

This skill implements Grace's design aesthetic:

**日式现代国际化设计 (Japanese Modern International Design)**
- Restrained, not minimal
- Structure and breathing rhythm
- Typography as the primary design element
- Generous white space
- Near-monochrome with one accent color

**NOT Silicon Valley SaaS Template:**
- No dark hero backgrounds
- No gradient text
- No floating light orbs
- No pill-shaped buttons
- No stock photos of people pointing at laptops

**Grace's Three-Cut Principle:**
1. **Typography** - Serif + sans-serif mix (headlines vs body)
2. **Layout** - Asymmetric + grid + square buttons + spacing
3. **Color** - Near-monochrome + 1 accent (only at key moments)

---

## Questions or Issues?

Open an issue at [github.com/Gracewillbe/super-distributor](https://github.com/Gracewillbe/super-distributor)

---

**A landing page is a conversion system, not an art project. Ship fast, iterate based on data.**
