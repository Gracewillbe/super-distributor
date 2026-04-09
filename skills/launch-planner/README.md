# Launch Planner Skill

Generate a complete launch plan with timeline, checklist, and ready-to-post content for all major platforms.

Based on [Chapter 07 - Launch Day](../../playbook/07-launch-day.md) from Super Distributor.

---

## What This Skill Does

The Launch Planner skill helps you plan and execute your product launch by:

1. **Gathering essential information** about your product and launch
2. **Creating a 2-week pre-launch checklist** with specific tasks
3. **Generating an hour-by-hour launch day timeline**
4. **Writing ready-to-post content** for all major platforms:
   - Twitter launch thread
   - Product Hunt description
   - Indie Hackers post
   - Hacker News "Show HN" post
   - Reddit post
   - Email to waitlist/beta users

**Everything is personalized** based on your product and ready to copy-paste.

---

## How to Use

### In Claude Code

1. Open your terminal in the Super Distributor directory
2. Run: `/skill launch-planner`
3. Answer the questions about your product
4. Get your complete launch plan

### What You'll Need

Have this information ready:
- Product name and one-liner
- Problem it solves
- 3-5 key features or benefits
- Launch date
- Product URL
- Pricing/access model

Optional but helpful:
- Why you built it (personal story)
- Any unique features to highlight

---

## What You'll Get

### 1. Pre-Launch Checklist

A detailed 2-week countdown with tasks organized by:
- 2 weeks before
- 1 week before
- 3 days before
- 1 day before

All actionable, all specific to your launch.

### 2. Launch Day Timeline

Hour-by-hour schedule from 6 AM to 11 PM, including:
- When to post on each platform
- What to do throughout the day
- How to engage with early users
- When to share updates

### 3. Platform-Specific Posts

Ready-to-post content for:

**Twitter:** 5-tweet thread with your story, features, and CTA

**Product Hunt:** Tagline + description optimized for PH audience

**Indie Hackers:** Post formatted for the IH community

**Hacker News:** Technical "Show HN" post

**Reddit:** Post template + recommended subreddits

**Email:** Subject line + body for your waitlist

### 4. Post-Launch Guide

What to do in the days and weeks after launch to sustain momentum.

---

## Example Output

See a sample output here: [example-output.md](example-output.md) *(coming soon)*

---

## Tips for Best Results

**Be specific:** The more detailed your answers, the better the output.

**Have your positioning clear:** If you haven't done positioning yet, use the [Positioning Playbook](../../playbook/03-positioning.md) first.

**Customize the output:** The generated content is a strong starting point, but add your own voice and style.

**Don't launch everything at once:** Pick 2-3 primary platforms and do them well. You can expand later.

---

## When to Use This Skill

Use Launch Planner when:
- ✅ You're 1-2 weeks away from launch
- ✅ Your product core feature works
- ✅ Your landing page is ready
- ✅ You need a concrete plan and content

Don't use it if:
- ❌ You haven't built anything yet (build first)
- ❌ You don't have a landing page (see [Chapter 05](../../playbook/05-landing-page.md))
- ❌ Your positioning is unclear (see [Chapter 03](../../playbook/03-positioning.md))

---

## Related Resources

**Super Distributor Playbooks:**
- [Chapter 03 - Positioning](../../playbook/03-positioning.md)
- [Chapter 04 - Messaging](../../playbook/04-messaging.md)
- [Chapter 05 - Landing Page](../../playbook/05-landing-page.md)
- [Chapter 07 - Launch Day](../../playbook/07-launch-day.md) *(this skill is based on this chapter)*
- [Chapter 08 - First Users](../../playbook/08-first-users.md)

**Other Skills:**
- `messaging-generator` — Turn positioning into copy *(coming soon)*
- `landing-page-builder` — Generate a landing page *(coming soon)*

---

## FAQ

**Q: Can I use this for a re-launch?**
A: Yes! Just mention it's a re-launch when answering the questions, and the skill will adjust the messaging.

**Q: What if I'm not launching on all platforms?**
A: Just tell the skill which platforms you want to focus on. It will generate content only for those.

**Q: Can I edit the generated content?**
A: Absolutely. The output is a starting point. Add your voice, adjust for your audience, and make it yours.

**Q: How long does this take?**
A: 10-15 minutes to answer questions and review output. Much faster than doing it from scratch.

---

## License

MIT — Part of Super Distributor

---

**Ready to plan your launch?** Run `/skill launch-planner` in Claude Code.
