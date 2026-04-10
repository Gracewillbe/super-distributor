# Super Distributor Roadmap

This document outlines the development roadmap for Super Distributor. All development happens in public — follow along, suggest priorities, or contribute.

---

## Current Status (April 2026)

**✅ Phase 1: Core Playbooks (Complete)**
- All 9 chapters live (~35,000 words)
- Full pathway from positioning to first 100 users
- README optimized as landing page

**🚧 Phase 2: Tools & Skills (In Progress)**
- 3 tools shipped (X auto-posting, Grok prompts, GitHub templates)
- 0 Claude Code skills (coming next)
- AI prompts library (planned)

**📋 Phase 3: Community & Growth (Planned)**
- Product Hunt launch
- Case studies and real-world examples
- Community contributions
- Translations

---

## Immediate Priorities (Next 2 Weeks)

### 1. Claude Code Skills (Top Priority)

Ship 3 core skills that turn playbooks into executable workflows:

#### `launch-planner` 🔴 Highest Priority
**Status:** Planned
**Target:** Week 1
**Chapter:** [07 - Launch Day](playbook/07-launch-day.md)

**What it does:**
- Input: Product name, description, launch date, target channels
- Output:
  - Pre-launch checklist (2-week countdown with tasks)
  - Launch day timeline (hour-by-hour schedule)
  - Ready-to-post content for all platforms:
    - Twitter thread
    - Product Hunt description
    - Indie Hackers post
    - Reddit post
    - Hacker News post
    - Waitlist email

**Why this matters:**
Launch day is the most stressful moment for indie makers. This skill turns Ch07 into an executable plan with all copy pre-written and ready to customize.

**Time estimate:** 3-4 hours to build

---

#### `messaging-generator` 🟢 High Priority
**Status:** Planned
**Target:** Week 1-2
**Chapter:** [04 - Messaging](playbook/04-messaging.md)

**What it does:**
- Input: Product positioning (problem, solution, differentiation)
- Output:
  - 3 one-liner variations (different formats from Ch04)
  - Value proposition (3-sentence version)
  - 3-5 core message pillars
  - Messaging hierarchy ready to use

**Why this matters:**
Most makers have decent positioning but struggle to turn it into actual words. This bridges the gap from strategy to copy.

**Time estimate:** 2-3 hours to build

---

#### `landing-page-builder` 🟢 High Priority
**Status:** Planned
**Target:** Week 2
**Chapter:** [05 - Landing Page](playbook/05-landing-page.md)

**What it does:**
- Input: Messaging output (from `messaging-generator` or manual)
- Output: Complete landing page HTML file
  - 5-section structure (Hero, Problem, Solution, How It Works, CTA)
  - Optional 7-section (+ Features, Social Proof, FAQ)
  - Grace's design aesthetic (Japanese modern, restrained, clean)
  - Single-file HTML, zero dependencies, mobile-responsive
  - Ready to deploy (Vercel / Netlify / anywhere)

**Why this matters:**
From zero to a live landing page in 30 minutes. The most tangible deliverable — people can ship something real immediately.

**Time estimate:** 4-5 hours to build

---

### 2. Skills Documentation
**Status:** Planned
**Target:** Week 2

- Usage guide for each skill
- Integration with existing playbooks
- Video walkthrough (optional)

---

## Medium-Term (Next 1-2 Months)

### Phase 2: Post-Launch Growth Skills (NEW - Based on Competitor Analysis)

After completing Phase 1 (core launch skills), add these high-value skills inspired by successful marketing tools on Agent Skills Hub:

#### `competitor-analyzer` 🎯 High Priority
**Status:** Planned
**Target:** Month 2
**Chapter:** [03 - Positioning](playbook/03-positioning.md)
**Inspiration:** ai-marketing-claude (competitive intelligence)

**What it does:**
- Input: Product description + competitor list (or auto-discover)
- Output:
  - Competitor matrix (features, positioning, pricing)
  - Differentiation analysis
  - Positioning recommendations
  - Gap opportunities

**Why this matters:**
Good positioning requires understanding the competitive landscape. This automates the research from Ch03 and helps identify your unique angle.

**Time estimate:** 3-4 hours to build

---

#### `email-sequence-builder` 🎯 High Priority
**Status:** Planned
**Target:** Month 2
**Chapter:** [08 - First Users](playbook/08-first-users.md) + [07 - Launch Day](playbook/07-launch-day.md)
**Inspiration:** ai-marketing-claude (email marketing automation)

**What it does:**
- Input: Product info + user journey stage
- Output: Complete email sequences:
  - Welcome series (3-5 emails)
  - Onboarding (feature education)
  - Nurture (engagement)
  - Re-engagement (win-back)

**Why this matters:**
After launch, you need to keep users engaged. Automated email sequences turn one-time visitors into active users.

**Time estimate:** 3-4 hours to build

---

#### `content-calendar` 🎯 High Priority
**Status:** Planned
**Target:** Month 2
**Chapter:** [06 - Social Media](playbook/06-social-media.md)
**Inspiration:** ai-marketing-claude (content planning)

**What it does:**
- Input: Product + target audience + posting frequency
- Output: 30/60/90-day content calendar
  - Topic ideas for each day
  - Content formats (thread, post, tutorial, case study)
  - Platform recommendations (Twitter, LinkedIn, Reddit)
  - Build-in-public storylines

**Why this matters:**
Consistent content builds audience and trust. A calendar removes "what should I post today?" paralysis.

**Time estimate:** 2-3 hours to build

---

### Phase 3: Optimization & Expansion Skills

Additional skills for when you have traction and want to optimize:

#### `seo-optimizer` 🟡 Medium Priority
**Status:** Planned
**Target:** Month 3
**Chapter:** [05 - Landing Page](playbook/05-landing-page.md)
**Inspiration:** seo-geo-claude-skills, marketingskills

**What it does:**
- Input: Landing page content or URL
- Output: Basic SEO optimization suggestions
  - Title tags and meta descriptions
  - Header structure (H1, H2, H3)
  - Keyword recommendations
  - Image alt text

**Why this matters:**
Basic SEO helps people find your landing page. Not deep technical SEO (that's for other tools), just the fundamentals.

**Note:** This is NOT a replacement for dedicated SEO tools. It's just landing page basics.

**Time estimate:** 2-3 hours to build

---

#### `cro-auditor` 🟡 Medium Priority
**Status:** Planned
**Target:** Month 3
**Chapter:** [05 - Landing Page](playbook/05-landing-page.md)
**Inspiration:** marketingskills (CRO)

**What it does:**
- Input: Landing page URL or HTML
- Output: CRO improvement checklist
  - CTA clarity and placement
  - Copy improvements (clarity, urgency, specificity)
  - Layout and visual hierarchy
  - Trust elements (social proof, testimonials)
  - Mobile optimization

**Why this matters:**
Once you have traffic, convert more of it. Small CRO tweaks can double your conversion rate.

**Time estimate:** 3-4 hours to build

---

#### `social-post-variations` 🟡 Medium Priority
**Status:** Planned
**Target:** Month 3
**Chapter:** [06 - Social Media](playbook/06-social-media.md)
**Inspiration:** ai-marketing-claude

**What it does:**
- Input: Core message + platform
- Output: 10+ variations from different angles
  - Problem-focused
  - Solution-focused
  - Story-based
  - Data-driven
  - Question-based
  - Contrarian

**Why this matters:**
Same message, different packaging. Test what resonates with your audience.

**Time estimate:** 2 hours to build

---

### Phase 4: Original Planned Skills

These were in the original roadmap and remain valuable:

#### `positioning-workshop`
**Chapter:** [03 - Positioning](playbook/03-positioning.md)
**What it does:** Interactive workshop to define positioning through guided questions
**Priority:** 🟡 Medium

#### `first-users-outreach`
**Chapter:** [08 - First Users](playbook/08-first-users.md)
**What it does:** Generate 10-10-10 daily plan + personalized DM templates
**Priority:** 🟡 Medium

#### `market-intel`
**Chapter:** [01 - Market Intelligence](playbook/01-market-intelligence.md)
**What it does:** Automate Reddit/Twitter research, summarize pain points and opportunities
**Priority:** 🟡 Medium

#### `social-post-generator`
**Chapter:** [06 - Social Media](playbook/06-social-media.md)
**What it does:** Turn ideas/updates into platform-specific posts (Twitter, LinkedIn, Reddit)
**Priority:** 🟡 Medium

---

### AI Prompts Library
**Status:** Planned
**Target:** Month 2

Pre-written prompts for common tasks:
- Positioning statement generation
- Copywriting for landing pages
- Launch post variations
- User interview questions
- Competitive analysis

**Format:** Markdown files in `prompts/` directory, organized by use case

---

### Tools Expansion

#### GitHub Launch Kit
**Status:** Planned
**Target:** Month 2

- Issue templates for user feedback
- PR templates
- README template for product launches
- GitHub Actions for launch automation

#### RedNote Distribution Tools
**Status:** Planned
**Target:** Month 3+

- Cross-posting scripts
- Chinese market research prompts
- RedNote-specific launch templates

---

## Long-Term (3+ Months)

### Case Studies & Real Examples
**Status:** Planned

- Document real product launches using Super Distributor
- Share results (traffic, users, conversion rates)
- What worked, what didn't
- Iterate playbooks based on real data

**First case study:** Capsule.ai launch (using Super Distributor to launch itself)

---

### Community Contributions
**Status:** Planned

- Accept community-contributed playbooks
- Translations (Chinese, Spanish, Japanese, etc.)
- Platform-specific guides (App Store, Chrome Web Store, etc.)
- Vertical-specific guides (SaaS, dev tools, design tools, etc.)

---

### Content Expansion

**Potential new chapters:**
- Pricing & monetization
- Retention (keeping your first 100 users)
- Scaling from 100 → 1,000
- Building in public strategies
- Community building

**Note:** Only add if validated by user demand. Don't bloat for the sake of more content.

---

## Distribution Channels

Where to submit Super Distributor skills and content for visibility:

**Skill Directories:**
- [ ] [Agent Skills Hub](https://agentskillshub.top/) — 52k+ AI agent tools directory
  - [ ] Submit `launch-planner` skill
  - [ ] Submit `messaging-generator` skill (when ready)
  - [ ] Submit `landing-page-builder` skill (when ready)
- [ ] Claude Code official skills repository (if exists)
- [ ] Awesome lists (awesome-claude, awesome-ai-tools, awesome-indie-makers)

**Launch Platforms:**
- [ ] Product Hunt (for Super Distributor itself)
- [ ] Indie Hackers "Show IH"
- [ ] Hacker News "Show HN"
- [ ] Reddit (r/SideProject, r/IndieDevelopers, r/SaaS)

**Content Platforms:**
- [ ] Dev.to (cross-post playbooks)
- [ ] Medium (if appropriate)
- [ ] Substack/Newsletter (weekly tips from playbooks)

**Community:**
- [ ] Twitter/X (regular sharing, not just launch)
- [ ] LinkedIn (B2B audience)
- [ ] Discord servers (relevant communities)

---

## Distribution Milestones

These are not "content" milestones, but distribution goals for the project itself:

**Month 1:**
- [ ] Product Hunt launch
- [ ] 500+ GitHub stars
- [ ] Featured on Indie Hackers
- [ ] Hacker News "Show HN" post
- [ ] 50+ pieces of user feedback

**Month 2:**
- [ ] 1,000+ GitHub stars
- [ ] 10+ community contributions (PRs, translations, case studies)
- [ ] First user success story ("I used this to get my first users")

**Month 3:**
- [ ] 2,000+ GitHub stars
- [ ] Active Discord/Slack community (if needed)
- [ ] Regular content updates (weekly/bi-weekly)

---

## How to Contribute

Want to help shape this roadmap?

**Suggest priorities:**
Open an issue with `[Roadmap]` in the title

**Vote on features:**
👍 React to existing issues

**Contribute:**
- Add case studies
- Build tools
- Translate playbooks
- Fix bugs or improve docs

**All contributions welcome.**

---

## Principles

This roadmap follows a few core principles:

1. **Ship fast, iterate based on feedback**
   Don't over-plan. Build, release, learn, repeat.

2. **Actionable over theoretical**
   Every addition should help someone ship faster or better.

3. **Free and open-source forever**
   No paywalls, no upsells, no "premium" tier.

4. **Built in public**
   Share progress, share struggles, share learnings.

---

**Last updated:** April 9, 2026
**Next review:** After shipping the 3 core skills

---

**Questions or suggestions?** Open an issue or start a discussion.
