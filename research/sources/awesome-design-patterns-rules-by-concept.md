# Design Rules by Concept

Harvested from the awesome-design-patterns list and the pages it recommends. Parts 1–11 come from the UI-patterns library and its persuasive (behavioral) patterns. Parts 12–18 cover front-end patterns: responsive design, CSS craft, CSS architecture, GUI architectures, React, Vue and mobile. Parts 19–26 cover software design principles, patterns and anti-patterns. Parts 27–40 cover architecture and system design. Everything is paraphrased. Entries tagged [general] or [general knowledge] were filled from well-established literature because the source page couldn't be read.

# Part 1 — Getting input

### Group: Forms

## 1. Drag and drop
- Problem: Users need to act on items by moving them from one place to another.
- Use when: A task works best as direct manipulation (reordering lists, moving objects, uploading files, rearranging layouts) without leaving the page.
- Let users grab items and drop them in the new position on screen.
- Use it for reordering, moving objects between containers, and file upload targets.
- Never make drag and drop the only way to rearrange things; also offer keyboard or menu-based moves for accessibility.
- Don't send users to a separate page just to reorder content.
- Why: Many users try dragging by instinct, and the physical metaphor gives very direct control. It is not fully accessible on its own, so it needs alternatives.

## 2. Structured format
- Problem: Users need to enter data quickly, but the data must follow a fixed structure.
- Use when: The input is a known type a program can parse (zip code, date, phone number, ID number) and full form controls would slow a frequent task.
- Show the expected format in the label or hint before the user types.
- Split long values into short, labeled segments (for example day/month/year, or the groups of an ID number).
- Offer helpers such as a date picker to fill the field correctly.
- Keep the format stable so people learn it and can type from memory.
- Don't use it for open-ended input with many interpretations; use Forgiving format instead.
- Why: Visible structure and chunking cut entry errors, speed repeated entry, and keep stored data clean.

## 3. Keyboard shortcuts
- Problem: Users repeating the same tasks lose time moving between keyboard and mouse.
- Use when: The app has frequent, repetitive actions.
- Assign shortcuts to the most frequent actions, not rare ones.
- Pick memorable letters (fall back to a middle or final letter of the action name if the first is taken).
- Place paired commands next to each other on the keyboard.
- Don't override operating-system shortcuts, shortcuts already used elsewhere in the app, or ones users have already built habits around.
- Advertise shortcuts in menus and tooltips, and offer a help overlay listing them.
- Why: Shortcuts let experts work faster with less effort while beginners can still use the mouse.

## 4. Captcha
- Problem: A site must verify that a submission comes from a person, not a bot.
- Use when: Anonymous visitors can post or register and automated spam is a real problem.
- Use a challenge that is easy for humans and hard for machines.
- Favour human readability over maximum bot resistance.
- Offer a refresh option and allow multiple attempts.
- Provide an audio (non-visual) alternative so visually impaired users are not locked out.
- Weigh the added friction against the actual spam risk before adding one.
- Why: It blocks automated abuse, but overly hard challenges frustrate users and exclude people with disabilities.

## 5. Rule builder
- Problem: Users repeatedly run searches or build segments based on their own sets of conditions.
- Use when: The number of conditions is unknown or users need saved, live segments; avoid it when a single text input or a fixed filter set suffices.
- Put each rule on its own visually separated row.
- Let users add and remove rules; place "Add" below the list or beside a rule to insert there.
- Offer a clear AND/OR (all/any) combinator, or mark each rule required or optional.
- Show a per-rule mini-form that fits the field type: text operators for text, dropdowns for lists, ranges for numbers.
- Save the rule definition rather than a static result so lists stay current.
- Why: Users can combine custom conditions, and saved rules keep returning up-to-date results as the data changes.

## 6. Inplace editor
- Problem: Users want to change a value quickly without leaving the page.
- Use when: Only one or a few simple values (text, dropdown) need editing.
- Edit the value where it is displayed instead of on a separate edit page.
- Signal editability on hover (highlight, tooltip, input-style outline).
- On click, swap in an input that matches the original font and size.
- Provide Save and Cancel; save asynchronously and return to the normal view.
- Don't mix editable text with links or action words; don't use it for many fields or complex formats.
- Why: Editing in context avoids a page change or popup, so small edits are cheap and stay tied to what the user sees.

## 7. Preview (live preview)
- Problem: Users want to see how their input will affect the final result before submitting.
- Use when: The output is hard to imagine from the inputs alone.
- Update the preview as the user changes fields, not only after submission.
- Process input in the client so the preview refreshes immediately.
- Render the preview in the same layout as the final output.
- Don't add a preview for simple inputs whose output doesn't depend on layout.
- Don't force a reload or submit just to check the input.
- Why: Immediate feedback removes doubt, so users commit with confidence and explore more freely.

## 8. Autosave
- Problem: Users want their work kept safe without having to remember to save.
- Use when: Users create content and should not worry about losing it.
- Save automatically at intervals or on events (field blur, navigation).
- Tune frequency to the app: frequent enough to be safe, not wasteful.
- Reflect save state in the save control (unsaved changes, then saved).
- Keep a save button even if it only closes the view; it reassures users.
- Don't save silently; leave a subtle visible trace. Consider pairing with Undo.
- Why: People can focus on creating instead of fearing data loss, and visible state builds trust.

## 9. Password strength meter
- Problem: Users choose weak passwords that are easy to guess.
- Use when: You want stronger passwords and want users to understand what makes one strong.
- Show a bar beside the field that fills and shifts from red to green as strength grows.
- Score against a few rules (length, mixed case, digits, symbols) and require only what your risk level needs.
- Avoid rigid complexity rules that push people to forgettable passwords or insecure workarounds.
- Also check server-side against dictionaries, which catch common substitutions that client rules miss.
- Steer users away from names, birthdays, keyboard runs, and single-character-type passwords.
- Pair the meter with a clear recovery path so strong passwords don't cause lockouts.
- Why: Live feedback nudges people toward better passwords and signals that the site takes security seriously; overly strict rules backfire.

## 10. Fill in the blanks
- Problem: Field labels often fail to explain what an input is for.
- Use when: Labels are vague, the context reads naturally as a sentence, there are few fields, and filling them is required or strongly encouraged.
- Embed the inputs inside a sentence, each blank acting as a field.
- Keep each blank one text line high; text boxes and dropdowns work best.
- Use it well for filters and conditions that read as a sentence.
- Don't use it for large forms or forms with many optional fields.
- Plan for localization, since word order differs between languages.
- Why: People understand sentences, so the form explains itself; translation is the main cost.

## 11. WYSIWYG
- Problem: Users want to publish formatted, media-rich content without writing markup.
- Use when: Users don't know markup, should see the published look while editing, or formatting should be easy.
- Replace a plain textarea with a rich-text editor.
- Show the content in its final formatted form while typing.
- Strip unneeded features (font colors, sizes, images) or restrict styles to predefined classes.
- Don't use it where clean markup is critical, since such editors often produce bloated output.
- Test across browsers; support can be uneven.
- Why: Word-processor-style editing removes the markup learning curve and builds confidence.

## 12. Input feedback
- Problem: After submitting, users need to know whether it worked and, if not, what to fix.
- Use when: Confirming success, reporting errors, or showing validation results.
- Validate for presence, format, length, exclusions, and uniqueness.
- On success, confirm clearly and ideally show the new item in context.
- On error, show a prominent summary at the top and highlight each failing field.
- Explain how to fix each error, in the summary or next to the field.
- Use color by meaning (green success, yellow neutral, red error); don't use red for minor issues.
- Prevent errors where possible (constrained controls) instead of only reporting them.
- Why: Users translate their mental data into the form's structure, so mismatches are common; clear, distinct feedback makes them quick to fix.

## 13. Calendar picker
- Problem: Users need to enter or filter by a date or a date range.
- Use when: Picking dates to submit, track, sort, or filter; skip it where typing is faster (birthdays far in the past).
- Open a month calendar from the field or a calendar icon, positioned near the input.
- Offer controls to move by month and year and to jump to today; make closing easy.
- Disable dates that violate business rules (past dates, weekends, beyond a booking window).
- Keep typed entry available and accept common formats.
- For ranges, push the end date forward when the start date passes it.
- Show full weeks, grey out (but keep selectable) adjacent-month days, and use large click targets.
- Why: Everyone knows how a calendar works, so picking dates and ranges becomes fast and accurate.

## 14. Morphing controls
- Problem: Showing controls that don't apply to the current mode clutters the interface.
- Use when: Controls are mutually exclusive or the UI has clear modes (play/pause, on/off, edit/view).
- Show only the action valid for the current state and swap it when the state changes.
- Make the most likely action the most prominent one.
- Keep typography and placement constant across states; color may change to signal state.
- Don't use it for actions users need to compare side by side or for state changes that are hard to notice.
- Why: Fewer visible controls means less noise and fewer decisions, and the changing control itself shows the current state.

## 15. Expandable input
- Problem: Users want maximum space for the main content with few distractions.
- Use when: Content matters more than optional input such as search, posting, or commenting.
- Show the input collapsed by default with a short hint of its purpose.
- Expand it to full size on focus or typing.
- Collapse it again when it is empty and loses focus.
- Don't hide it so well that users can't find it.
- Why: Keeping inputs compact until needed frees space for content and reduces clutter.

## 16. Settings
- Problem: Users need one central place to configure how the application behaves.
- Use when: A preference is needed by many, must be reachable for some, or is rarely changed.
- Group related settings into clear sections; move minor ones to subscreens.
- Scale structure to size: no grouping at around 7 or fewer options, dividers at roughly 9 to 16, subscreens beyond that.
- Show current values at a glance, with the most-used settings first.
- Choose low-risk defaults most people would pick.
- Title each subscreen exactly like the setting label that opens it.
- Don't put frequent actions in settings; put them in a toolbar.
- Why: Predictable, well-grouped settings let people customize without hunting or feeling overwhelmed.

## 17. Forgiving format
- Problem: Users want to type data quickly in their own way and let the system interpret it.
- Use when: Explicit controls would be tedious and the input is a narrow, parseable domain (locations, times, durations).
- Accept many common formats for the same value.
- Parse typical word and number patterns into structured values.
- Give an example or short hint to guide input.
- Don't use it for open-ended input or input a program cannot reliably interpret.
- Why: It saves space and effort, letting users focus on their goal instead of a strict format; success depends on a narrow domain and clear prompting.

## 18. Undo
- Problem: Users make mistakes and need to reverse their own actions.
- Use when: Users should explore freely or losing work would be costly.
- Make reversing an action easy and immediate.
- Support multiple undo steps.
- Prefer undo over confirmation dialogs for reversible actions.
- Add undo anywhere work could be lost.
- Why: Knowing mistakes are reversible encourages experimentation and faster learning; the costlier the loss, the more undo matters.

## 19. Input prompt
- Problem: A field's label may not make clear what to enter.
- Use when: Labels need help or space is tight.
- Prefill the field with example text or a question showing what to enter.
- For dropdowns use "Select..." or "Choose..."; for text fields start with a verb (Enter, Type, Search) and end with the noun requested.
- Clear the prompt on focus so the user can type.
- Don't use the prompt as a substitute for a visible label where context is needed; avoid it on long or complex forms.
- Why: In-field prompts catch skimming eyes and save space, but disappearing text means users can forget what a field asked for.

## 20. Good defaults
- Problem: Long forms feel tedious when most users would choose the same values anyway.
- Use when: Many choices are required and the system can guess likely answers; avoid it for choices that need deliberate consent.
- Preselect or prefill the most likely value based on context or common usage.
- Base guesses on known signals (location, browser language, earlier answers).
- Only default when you are confident most users would accept it; wrong defaults add work.
- Keep defaults visible and easy to change.
- Never preselect consent, newsletter, privacy, or cost-bearing options, or defaults that favour the business over the user.
- Why: Defaults remove effort and reduce abandonment; even an imperfect default is an editable starting point.

### Group: Explaining the process

## 21. Wizard
- Problem: A user's goal breaks into dependent sub-tasks, often in a fixed order.
- Use when: The task has ordered steps, later steps depend on earlier choices, or users lack domain knowledge.
- Show one focused step at a time with total steps, current position, and completed steps.
- Provide Previous/Next and Finish on the last step; add a visually separated Cancel that warns before discarding data.
- Keep each step above the fold; split steps that force scrolling, but don't add so many screens that it drags.
- Use plain language and sensible defaults.
- Summarize choices before Finish with links back to edit.
- Don't make the wizard the only path; give experts a faster alternative.
- Why: Chunking a complex task reduces errors for novices, but long or opaque wizards frustrate and hide the underlying decisions.

## 22. Inline help box
- Problem: Users need guidance right next to the interaction they're about to do.
- Use when: An interaction isn't self-evident or you want to orient new users.
- Place a short help block above or below the main content of the screen.
- Style it with a distinct background so it reads as guidance, not functionality.
- Add a dismiss control that hides it permanently.
- Offer a way to re-enable all dismissed help.
- Prefer contextual help over sending users to separate FAQ pages.
- Why: Contextual tips are absorbed more easily than detached documentation, and dismissal keeps the UI clean for experienced users.

## 23. Steps left
- Problem: In a multi-step flow, users need to know where they are and how much remains.
- Use when: The process is long enough to feel endless; skip it for one or two obvious steps.
- Show a step list that stays visible on every step.
- Highlight the current step and update as the user advances.
- Communicate remaining effort with step counts, a progress bar, or both.
- Strip extra navigation, ads, and distractions from the flow.
- Why: A visible endpoint keeps users focused on finishing, especially in checkout and sign-up.

## 24. Completeness meter
- Problem: Users pursuing a goal need to know how to reach it and when it is done.
- Use when: You want users to complete optional-but-valuable tasks, such as a profile or onboarding.
- Break the goal into small, easy sub-tasks.
- Show a percentage or bar that rises with each completed task.
- Link to the next task so momentum continues.
- Mark 100% clearly; optionally reward it (badge, announcement).
- Don't use it for critical goals or strictly sequenced tasks; avoid starting values so low they discourage.
- Why: Curiosity and a visible feedback loop linking each action to progress motivate completion.

### Group: Community driven

## 25. Pay to promote
- Problem: Users want to pay to lift their content above the regular feed.
- Use when: You want to let people bypass ranking for reach, or offer paid boosts as revenue.
- Let users pay to boost a post or profile above organic content.
- Style boosted items like native feed items.
- Always label promoted items clearly as sponsored.
- Don't make paid items indistinguishable from organic ones.
- Offer audience targeting when useful; keep organic ranking intact for unpaid content.
- Why: It earns revenue and gives users reach, and clear labeling protects trust.

## 26. Rate content
- Problem: Users need to judge which content is worth their time or money.
- Use when: You have a large, active community whose judgments you trust.
- Allow one rating per user on a numeric scale (for example 1 to 5) and confirm it was recorded.
- Show the average rating per item.
- Allow optional written reasons.
- Surface top-rated items on main pages, in search, tags, and related items.
- Be explicit about what is being rated, or split into sub-ratings (product, seller, price).
- Don't use it in small communities; guard against manipulation with rate limits and weighting trusted users.
- Why: Ratings reduce the risk of wasting time or money and let the community separate good from weak content.

## 27. Vote to promote
- Problem: A community needs to decide collectively which content is most valuable.
- Use when: The community is large enough to generate meaningful vote counts.
- Allow one vote per user per item, and let users change or retract it.
- Show vote counts for easy comparison.
- Surface top-voted items on the home page, in search, tag pages, and related lists.
- Show users their own vote history.
- Rate-limit votes and cap repeated downvoting of one person's content.
- Why: Voting curates at scale without paid editors, though popularity is not always quality.

## 28. Wiki
- Problem: Users need a shared space to create and maintain information together.
- Use when: Users should contribute to content, or a document collection must stay current.
- Let anyone permitted edit existing pages and create new ones.
- Version every page so changes can be rolled back.
- Make creating, editing, and linking pages easy.
- Use a simple in-browser markup.
- Don't use it for publisher-controlled content (legal, terms) or time-bound content (news, posts).
- Why: Collaborative editing keeps knowledge current without one author, and version history makes openness safe.

## 29. Flagging and reporting
- Problem: Users need a way to mark inappropriate content for moderator review.
- Use when: User-generated content volume exceeds what staff can review.
- Give every piece of content a simple report action.
- Route reports to moderators who decide on removal or recategorization.
- Use reports to prioritize moderation rather than relying on staff to find problems.
- Don't launch a UGC community without flagging.
- Why: Community flagging distributes moderation across users, most of whom are willing to help.

# Part 2 — Onboarding

### Group: Getting in

## 30. Account registration
- Problem: You need to know who the user is to personalize content, restrict access, or let them buy.
- Use when: Access must be controlled, context should follow the user, or user data must be protected.
- Make sign-in and sign-up prominent; never bury the sign-in form.
- Offer sign-up at several points of action, not only one.
- Let people browse first; ask for an account only when they try to do something that needs it.
- Keep password rules simple and proportional to the data's sensitivity.
- Ask only for what you need, explain why, offer social login, and return users to where they were after login.
- Why: Accounts enable personalization and stored data (wish lists, billing) and show who uses the product.

## 31. Social login
- Problem: Users don't want to create and remember yet another password.
- Use when: Your audience already has accounts with a trusted identity provider, especially on mobile.
- Show one to three provider buttons above the email form; keep email sign-up available.
- Offer only providers your users actually use; long logo rows add decisions.
- Request minimal data (name, email); ask for more later with a reason.
- Prefill from provider data and never ask again for what you already received.
- Use each provider's standard button and label; never post on the user's behalf without asking.
- Why: One familiar click replaces several fields, and recognition beats password recall.

## 32. Magic login link
- Problem: Users want to sign in without creating, remembering, or resetting a password.
- Use when: Sign-ins are infrequent and users can reach their email on the same device.
- Ask only for an email, then send a one-time link or short code.
- Say what happens next (sender, subject, expiry) and offer resend and address correction.
- Offer a code alongside the link so users can finish on any device; return them to where they were.
- Keep sessions alive reasonably long; make links single-use and short-lived.
- Don't use it for frequent sign-ins, shared devices, or unreliable email delivery.
- Why: It removes the password burden and verifies the email in the same step.

## 33. Deferred verification
- Problem: Forcing email confirmation at sign-up sends eager users away to their inbox, and many never return.
- Use when: The first session is useful without a confirmed address; avoid it where unverified accounts enable abuse.
- Let users into the product immediately and send the confirmation in the background.
- Show a dismissible banner with resend instead of blocking screens.
- Explain what verifying unlocks and ask next to that feature.
- Gate only actions that affect others or cost money (inviting, publishing, paying, exporting).
- Return users to their work after confirming.
- Why: Verification serves the system more than the user; asking after they've invested makes it easier to accept.

## 34. Lazy registration
- Problem: Users want to try a product before registering.
- Use when: Sign-up feels like a big commitment, the product costs money, or users are comparing alternatives.
- Let users use a meaningful subset of features before signing up.
- Start them on real work (a cart, a document) so registering is a small step to keep it.
- Consider a background anonymous account persisted by cookie.
- Ask for registration only after users have invested effort.
- Show value clearly and make account access easy to find later.
- Why: People who have already invested time and seen value are far more likely to register to keep their work.

## 35. Guest access
- Problem: Recipients of shared content must register before viewing, so many never do.
- Use when: Recipients only need to view, comment, approve, book, or reply, and the item stands alone.
- Open the shared item directly, not a marketing page.
- Show who sent it and a short note on why it matters.
- Let recipients take the first action without an account.
- Offer sign-up later, tied to a clear benefit (saving, notifications), and keep guest activity on conversion.
- Don't use blurred previews or walls; protect sensitive content with expiry and permission limits.
- Why: Recipients see the product working before any commitment and are more likely to convert.

## 36. Onboarding carousel
- Problem: Intro screens explaining the product are swiped past unread.
- Use when: One key concept or a permission needs explaining before the first screen makes sense.
- Keep it to three screens or fewer.
- Give each screen one user benefit: a headline plus one line.
- Show real product screenshots, not stock illustrations.
- Provide back/forward, a progress indicator, and skip/close.
- Don't list features without benefits; end with a clear action into the product.
- Why: It sets expectations when users are receptive, but only short, concrete screens are remembered.

## 37. Welcome screen
- Problem: Right after sign-up users need confirmation and a clear next step, especially in an empty product.
- Use when: Users arrive from different promises or the next step isn't obvious; skip it if they can land straight in a meaningful action.
- Greet by name and say in one sentence what the space is for.
- Echo the promise that brought them in, and reflect invite/template/campaign context.
- Offer one primary next step, or a few distinct starting routes.
- Don't turn it into a feature tour or chain of modals; don't show it at every login.
- Why: Confirming the decision just made builds commitment and gives direction at peak uncertainty.

### Group: Setting up

## 38. Personalization form
- Problem: One generic onboarding path doesn't fit users with different goals, roles, and expertise.
- Use when: Distinct use cases exist and answers will visibly change what users see; skip it if answers only feed marketing.
- Ask one to three short questions at the start.
- Offer a few large labeled options, include "Other", and allow skipping.
- Explain briefly why you ask and what users get.
- Make every answer change something visible (template, first task, sample data); delete questions that change nothing.
- Show the tailored start immediately and let users change answers later; leave sales/attribution questions out.
- Why: Tailored first steps fit each user, and choosing a path creates a small commitment to follow it.

## 39. Smart prefill
- Problem: Setup asks users to type details the product could infer.
- Use when: Reliable signals exist (email domain, social login, device locale, location) and guesses are easy to verify.
- Prefill inferred values and let users confirm or change them.
- Use only signals users would expect you to have, and be able to explain each source.
- Mark values as detected and show them before submission.
- Clean guesses first (strip aliases, fix capitalization).
- Don't prefill sensitive or unreliable data or pre-check access-widening options.
- Why: Confirming is cheaper than typing, and accurate guesses signal attentiveness, while wrong ones erode trust.

## 40. Connected accounts
- Problem: The product needs data from other tools, but connecting accounts feels technical and risky.
- Use when: First value depends on another service (calendar, storage, tracker).
- Recommend the one or two most relevant integrations with recognizable logos, plus "see all".
- Make each connection one clear action.
- Explain what you will read or do, and what you won't, before the provider's consent screen.
- Request the narrowest scope needed.
- Show imported results right away; keep the step skippable and reversible.
- Why: Explaining limits lowers perceived risk, and immediate results justify the effort.

## 41. Data import
- Problem: Switchers arrive at an empty product, and rebuilding their work keeps them on the old tool.
- Use when: Users come from spreadsheets or competitors and value depends on their data; avoid fragile imports that would damage trust.
- Offer import as a primary start option beside blank and template.
- Accept the formats and competitor sources users actually have (upload, select, paste).
- Ask during setup which tools they use so the right path appears.
- Preview items and auto-map fields with user correction before committing.
- Run large imports in the background, report successes and failures, never fail silently, and allow reversal.
- Why: Taking over switching effort gets users to value on their own material fast.

## 42. Role-based invite
- Problem: Inviters hesitate when they can't tell what access they're granting, and invitees land in the wrong view.
- Use when: People have different roles or oversharing is risky.
- Let the sender pick a role in the invite dialog from three or four plainly named roles with short descriptions.
- Show current collaborators and roles, and keep link access as a separate setting.
- Preselect the lowest role that still lets the invitee do the expected task.
- Never default to broad permissions.
- Send each invitee to a first screen suited to their role.
- Why: Clear permissions remove the guesswork that blocks invites, and role-specific entry gives recipients context.

## 43. Permission priming
- Problem: The OS permission dialog gives no context, and users who decline are hard to win back.
- Use when: A feature needs a system permission whose benefit isn't obvious at that moment.
- Show your own explanation screen before triggering the system dialog.
- Ask when the user reaches for the feature, not at launch.
- State the user benefit in one sentence.
- Tell users what the system prompt will look like.
- Keep a visible decline option; never disguise your screen as the system dialog.
- Why: A no on your screen doesn't burn the one-time system prompt, and timely reasons increase acceptance.

### Group: Finding your way

## 44. Playthrough
- Problem: Users must learn core features before they get value.
- Use when: Core interactions should be practiced before entering the full product, or setup is needed before the app works.
- Build a safe starter space for practicing core actions.
- Add brief hints and simple goals so users learn by doing.
- Carry earned progress into the real product.
- Always offer skip; keep it to essentials and let users leave anytime.
- Why: Users build skills and early wins without facing failure they aren't ready for.

## 45. Guided tour
- Problem: Users need to learn new or unfamiliar features.
- Use when: The interface isn't self-explanatory or new features need introducing to existing users.
- Trigger hints (tooltips, overlays, modals) when users reach the relevant point.
- Choose between a linear product-led tour and context-triggered user-led hints.
- Don't overload users with many or bland hints.
- Make the tour easy to dismiss and show completion state.
- Why: Paced, contextual guidance teaches without overwhelming people who don't want help.

## 46. Walkthrough (tour)
- Problem: Prospects want to understand a product before joining or buying.
- Use when: Users need to see what the product offers and how common tasks work before committing time or money.
- Present core benefits before real use, and keep it short.
- Focus on user goals, not every feature.
- Use screenshots, illustrations, or short videos.
- Link each section to the matching part of the product.
- Address top concerns early (security, import/export).
- Why: It lets users judge fit without signing up.

## 47. Coachmarks
- Problem: Users struggle with a complex or unfamiliar interface.
- Use when: The interface is complex and cannot be simplified enough.
- Overlay a dimmed layer with short tips and arrows pointing at specific controls.
- Keep tips brief and placed so they don't hide their target.
- Limit to a few tips.
- Fix core usability first; don't use coachmarks to paper over bad design.
- Don't interrupt mid-task; consider playthroughs or interactive tours instead.
- Why: Overlays explain without fixing root problems and add a blocking mode that strains memory, so use sparingly.

## 48. Hotspot
- Problem: Optional features are hard to explain without interrupting focused users.
- Use when: A secondary feature should be discovered at the user's own pace.
- Place a small, slowly pulsing dot next to the feature; keep motion calm.
- On click or hover show a one-sentence tip with an optional action.
- Remove the dot once opened or the feature is used; give tips a clear close.
- Show at most one or two per screen; never use hotspots for must-act information.
- Why: Curiosity draws users in on their own terms while pointing right at the feature.

## 49. Inline hints
- Problem: Users need to learn features without being blocked or interrupted.
- Use when: Guidance shouldn't obscure content, or alongside blank slates.
- Style hints like surrounding content so they blend in.
- Keep hints relevant to nearby content.
- Don't use hints for critical instructions or messages users must notice.
- Don't overuse them; use them to reinforce guidance given elsewhere.
- Why: Hints formatted as normal content are easy to read and feel relevant.

## 50. Onboarding checklist
- Problem: New users can't tell which actions lead to real value.
- Use when: Value depends on a few setup/usage actions spread over sessions, and you know which predict retention.
- Show 3 to 7 goal-phrased tasks, quickest value first, with visible progress.
- Make each task a shortcut to where it is done and auto-check it when completed anywhere.
- Pre-check something already done to create momentum.
- Keep it compact, dismissible, and retire it when complete.
- Never list business goals or tick tasks the user hasn't done; pick tasks from retention data.
- Why: A finite visible path increases effort near the goal, and unfinished items pull users back.

## 51. Feature spotlight
- Problem: Users never discover features they haven't used.
- Use when: A feature fits the user's current work, or they're using a slow workaround.
- Trigger the spotlight from behavior (for example repeating a manual task).
- Match the format to the feature: inline hint, small "New" badge, or modal only for major changes at session start.
- Target users working in the related area.
- Link directly to the feature.
- Don't interrupt a task; remove the badge once tried or after a few sessions.
- Why: It extends onboarding beyond the first sessions by tying features to the user's own work.

### Group: Reaching first value

## 52. Blank slate
- Problem: An empty screen doesn't tell new users what it will hold or what to do.
- Use when: A section has no data yet (first use, after clearing).
- Show a sample or preview of the filled state.
- Add short getting-started help.
- Answer "what is this" and "what do I do next".
- Provide one clear starting action.
- Don't leave it bare, and don't overload it with options.
- Why: Guided empty states set expectations, reduce intimidation, and build early trust.

## 53. Template gallery
- Problem: An empty canvas leaves users unsure what good looks like.
- Use when: Users create documents, boards, or workflows that follow reusable structures.
- Offer ready-made starters that open in one click and can be adapted.
- Show a visual preview of each template, not just its name.
- Show a small goal-matched set in onboarding; categorize and search the full collection.
- Fill templates with realistic sample content.
- Keep a "Blank" option; avoid long undifferentiated lists.
- Why: Editing is easier than creating, and adapting a template teaches the product's structure.

## 54. Suggested action
- Problem: After a step or on an empty page, users don't know what to do next and momentum fades.
- Use when: There is one clear next step that follows from the user's progress.
- Show one primary suggestion with a short reason, placed where attention already is.
- Make it the most prominent element.
- Start with quick, low-risk steps that give a result before commitment.
- Let users dismiss it and don't bring it back unchanged.
- Don't lead with upgrades or invites before value; don't offer a list of equal options.
- Why: One clear next move reduces decision effort and keeps engagement going.

## 55. Success state
- Problem: Users miss their first meaningful win, so it fails to build confidence.
- Use when: A meaningful first action has just completed and the result isn't obvious.
- Name the win in the user's terms, not a generic "Success!".
- Show the actual result beside the message.
- Offer one clear next step.
- Scale celebration to real milestones; skip it for trivial actions.
- Never block progress or confirm success before it actually happened.
- Why: People judge experiences by their endings, and an honest win reinforces competence.

### Group: Coming back

## 56. Streak counter
- Problem: Repetition is invisible, so each return feels like a fresh decision.
- Use when: Value comes from regular behavior (exercise, learning, writing) and missed days are recoverable.
- Show the streak next to the action that maintains it, with a clear prompt at zero.
- Match the unit to the behavior (daily vs. weekly with rest days).
- Show the pattern (calendar/grid), not just a number.
- Allow recovery (freezes, restarts that keep history); avoid "you're behind" language.
- Don't use it for irregular behavior or where losing a streak causes anxiety; celebrate modestly.
- Why: Streaks make effort visible and give a reason to return, but loss aversion can turn them into pressure.

## 57. Reminder scheduler
- Problem: Users intend to return but the intention fades without a set time.
- Use when: Value depends on recurring routine use.
- Ask when users will return, not just whether they want reminders.
- Offer a time plus a few day groupings (weekdays, every day).
- Suggest a routine-linked time when known, but don't impose a default.
- Ask right after a success; confirm the reminder is saved.
- Provide an easy off switch and stop reminding when it no longer helps.
- Why: Naming a specific time turns a vague intention into a plan people follow.

### Group: AI features

## 58. Suggested prompts
- Problem: An empty prompt box leaves users unsure what the system can do.
- Use when: The product takes open-ended natural-language input and users are new.
- Show a few clickable example requests near the empty box.
- Write each as a complete request that yields a good result.
- Base examples on common tasks or the user's current context.
- Clicking fills the box for editing rather than sending immediately.
- Refresh suggestions as context changes; avoid generic or show-off examples.
- Why: Choosing is easier than inventing, and examples teach good request structure.

## 59. Refinement controls
- Problem: Users abandon AI features after the first output because they don't know they can refine it.
- Use when: Output is a draft that usually needs adjusting; skip it for single-correct-answer output.
- Put actions such as regenerate and variations beside each result.
- Offer three to five common adjustments as buttons ("Shorter", "More formal").
- Include a free-form refinement field.
- Allow direct editing and returning to earlier versions.
- Make clear whether a refinement replaces or adds a result; don't overload with controls.
- Point out the controls right after the first result.
- Why: Controls turn a weak first result into a next step and teach that AI work is iterative.

## 60. Source citations
- Problem: Users can't tell which parts of an AI answer to trust or verify.
- Use when: Output draws on documents, data, or the web and errors matter.
- Attach a citation marker per claim, linked to its source.
- List sources with recognizable titles and domains.
- Separate inferred conclusions from facts read directly.
- Express confidence in plain words, not percentages.
- Never cite sources that don't support the claim; group markers by sentence or paragraph to avoid clutter.
- Why: Calibrated trust survives the first visible error; blanket trust does not.

### Group: Upgrades and exits

## 61. Feature gate
- Problem: Paid features are either hidden or locked without explanation.
- Use when: A paid feature would clearly help the current task in a free tier; never gate the first experience of value.
- Keep the paid feature visible in place with a small badge (Pro, lock).
- Show what it would do with the user's own work or a realistic sample; offer a trial.
- State the unlocking plan, price after trial, and trial end; remind before it ends.
- Don't scatter gates so widely the free product feels like an ad; keep the core complete.
- Make the gate easy to dismiss and return to the task.
- Why: Value shown in context at the moment of need persuades better than a pricing page.

## 62. Paywall
- Problem: Users must pay to access restricted content.
- Use when: Content value exceeds price and you want direct revenue; avoid if income depends on ad pageviews.
- Choose a model: hard lockout, freemium, metered allowance, time passes, bundles, or per-item.
- Consider non-cash access where it fits (existing subscriptions, contact permission, surveys).
- Preview the locked content so value can be judged.
- Always state the price and the ways to get access.
- Why: Ads alone often no longer fund online content, so paywalls replace lost revenue.

## 63. Usage meter
- Problem: Users hit plan limits without warning, mid-work.
- Use when: The plan caps seats, storage, credits, or actions that normal use can reach.
- Show "used of total" with a small bar per limit, naming what is counted and when it resets.
- Place it in settings or sidebar and link to plans.
- Warn at about 80%, explaining options: upgrade, free space, or wait.
- At the limit, block only the next action so current work can finish.
- Don't use alarming colors, flashing, or countdowns to pressure upgrades; reserve red for reached limits.
- Why: Predictable limits let users choose when to upgrade.

## 64. Trial countdown
- Problem: Trial endings surprise users with charges or lost access.
- Use when: A time-limited trial is followed by a charge or loss of access.
- Show days left in a small persistent element, stated plainly.
- Link it to a page explaining what happens at the end and the options.
- Send a reminder a few days before, stating any charge amount.
- Pair the countdown with what the user has accomplished.
- Never invent deadlines, reset timers, or use "last chance" pressure.
- Why: Honest timing gives users control and builds lasting trust.

## 65. Cancellation flow
- Problem: Leaving users get generic retention offers or deliberate obstacles.
- Use when: Users can cancel a subscription or close an account.
- Put cancel where users look (account/billing) and name it plainly.
- Ask one optional reason question, then offer a fitting alternative (pause, cheaper plan, support).
- Show offers beside the exit button, never in front of it.
- Don't hide links, stack confirmations, or use guilt copy.
- Explain what data is kept or deleted, offer export, require a deliberate confirm, and close with clear feedback.
- Why: Matched offers keep users who would stay; a clean exit earns trust and future return.

# Part 3 — Navigation

### Group: Tabs

## 66. Navigation tabs
- Problem: Site sections need flat, simple navigation that shows where the user is.
- Use when: About 2 to 9 sections with short names and a clear current section; avoid it for dynamic content or lists needing "more".
- Place main sections in a horizontal bar of button-like tabs.
- Make the whole tab clickable, not only the label.
- Keep tabs persistent and in the same order on every page.
- Highlight the active tab; optionally add a connected sub-section bar beneath it.
- Don't use tabs for dynamic content such as latest articles.
- Why: The folder-tab metaphor is familiar, shows what's available, and marks the current place.

## 67. Module tabs
- Problem: Several sections must share one display area and switch without reloading.
- Use when: Space is tight and there are 2 to 9 similarly structured, independently readable sections with short labels.
- Show the sections in one shared content box with one row of tabs above.
- Keep the tab bar to a single line; never stack rows.
- Mark the active tab visually.
- Swap only the content and active state on click, without a page load.
- Don't use it when sections deserve their own pages.
- Why: Tabs group similarly structured content by category in a familiar way and keep attention without reloads.

### Group: Jumping in hierarchy

## 68. Breadcrumbs
- Problem: Users need to see where they are in a hierarchy and move back up.
- Use when: The site has a strict hierarchy and users often land deep from search or external links.
- Show the path of section labels from top level to the current page.
- Link every ancestor; leave the current page as unlinked text at the end.
- Separate items with a character such as > or », unlinked.
- Match labels to actual section titles.
- Don't show breadcrumbs on the top page, and never as the only navigation.
- Why: They reveal position in the structure and give quick upward routes in minimal space.

## 69. Fat footer
- Problem: Users need quick access to sections without walking the hierarchy.
- Use when: Popular pages and functions sit at different depths.
- Use the same footer layout on every page.
- Include expected items: about, terms, privacy, contact, sitemap-style links, address, social.
- Add shortcuts to your most-used pages regardless of depth.
- Don't rely on it as main navigation or overload it.
- Why: It offers a natural next step at the end of a page, keeping users engaged with fewer clicks.

## 70. Modal
- Problem: Users must act on or dismiss an overlay before returning to the page.
- Use when: Something important justifies interrupting the current task.
- Present content in a blocking overlay until closed.
- Match the confirm button label to the modal title so the source is clear.
- Provide several exits: X in the corner, Cancel/Close, Esc key, click outside.
- Don't use modals for error, success, or warning messages.
- Avoid modals on mobile where screen space is scarce.
- Why: Modals command attention, but forced interruptions frustrate and extra modes confuse.

## 71. Notifications
- Problem: Users can miss important updates and messages.
- Use when: Time-sensitive, personally relevant information must reach a user who is focused elsewhere.
- Notify only about timely, relevant events and tune frequency.
- Make notifications dismissible and configurable or disableable in settings.
- Sync read state across devices.
- Group same-type notifications into one summary with a count.
- Add quick actions only if useful, unambiguous, and distinct from the default click.
- Don't notify about content already on screen, background sync, or errors the user can't act on.
- Why: Notifications interrupt by nature, so relevance, timing, and control decide whether they help or annoy.

## 72. Shortcut dropdown
- Problem: Users want fast access to a specific section without traversing the hierarchy.
- Use when: A few destinations are used far more than others or sit at different levels.
- Provide a dropdown listing a fixed set of destinations.
- Navigate on selection or on submit.
- Include only the most-used destinations.
- Don't use it as main navigation.
- Why: Direct links to common destinations cut clicks and confusion.

## 73. Home link
- Problem: Users need a dependable way back to a safe starting point.
- Use when: Users often land on interior pages.
- Link the logo to the home page on every page, in a consistent position.
- If there is no logo, add a text "Home" link.
- Distinguish site root from section homes when both exist.
- Don't rely on the logo alone; add an explicit Home link near main navigation.
- Why: Logo-as-home is a strong web convention, but not every user recognizes it.

### Group: Menus

## 74. Vertical dropdown menu
- Problem: Users must move among sections when navigation space is limited.
- Use when: Roughly 2 to 9 hierarchical sections, or a desktop-application feel; use tabs if the current section must be highlighted.
- Put main sections in a horizontal row that reveals a vertical submenu on hover.
- Delay closing by about 200 to 300 ms after the cursor leaves.
- Make hover areas wider than the text and change the cursor on hover.
- Render the menu in HTML, not only client-side script, so it is indexable.
- Why: Dropdowns save space and keep top-level items visible while exposing deeper levels.

## 75. Accordion menu
- Problem: Users need to move between main sections and reach subsections elsewhere.
- Use when: Sidebar navigation with fewer than 10 sections, each with 2 or more subsections, and only two levels.
- Give each heading a panel that expands to show subsections.
- Collapse other panels when one opens.
- Expand the relevant section when the user navigates to it, so content isn't hidden from find-in-page.
- Don't use it where users switch between distant sections often.
- Why: Accordions pack many options into little space but make frequent long jumps tedious.

## 76. Horizontal dropdown menu
- Problem: Navigation space is limited but there are hierarchical sections.
- Use when: 2 to 9 sections with sub-levels, or a desktop-app feel.
- List main sections in a vertical strip and reveal submenus beside the item on hover or click.
- Delay hiding submenus by about 200 to 300 ms; avoid instant-hide.
- Make hit areas wider than the text and change the cursor on hover.
- Don't use it to indicate the current section (use tabs), and don't build it in script only.
- Why: Dropdowns save space but are often fiddly, so forgiving hover behavior is essential.

### Group: Content

## 77. Adaptable view
- Problem: The default presentation doesn't fit every user's device, ability, or preference.
- Use when: Many users have specific needs (small screens, low vision, color blindness, mobile vs. full site).
- Provide an on-page control to switch or adjust the presentation.
- Don't rely only on device detection; let anyone pick any view.
- Don't assume users know browser zoom or custom stylesheets.
- Persist the choice across visits.
- Offer an easy switch between mobile and full versions.
- Why: Users get presentation that fits them and never feel stuck in a version they didn't choose.

## 78. Article list
- Problem: Hierarchical navigation alone doesn't lead readers to stories they'll care about.
- Use when: Guiding readers to editorial content such as news.
- Keep teasers scannable and drop decorative clutter.
- Make headlines visually distinct from subheads; add category labels for context.
- Group long lists by date, category, or tag rather than numbered pages.
- Show author or comment counts only when meaningful; never show "0 comments".
- Make the whole teaser clickable with a clear call to action.
- Choose featured stories from the reader's perspective, not your own.
- Why: Teasers drive continued browsing on editorial sites.

## 79. Tagging
- Problem: Items need keywords to label and organize them.
- Use when: Content fits several categories rather than one hierarchy, or users organize their own content.
- Let users attach multiple keywords per item.
- Use descriptive, categorizing terms.
- Make tags searchable and render them as links to related items.
- Keep tags flat; don't force a hierarchy.
- Why: Tags organize bottom-up and help people find their own and others' related content.

## 80. Pagination
- Problem: Users need to view a sorted dataset in digestible pieces.
- Use when: Data is too large for one page and has a meaningful order.
- Split into sequential pages, each with its own link.
- Provide previous/next and first/last; show "last" only when the total is known.
- Place controls below the list so users pause and decide whether to continue.
- Don't use it where users should flow through content without pausing.
- Why: Chunks are easier to digest, load less at once, and show how much remains.

## 81. Categorization
- Problem: Users want to make sense of content by browsing it in groups.
- Use when: Content naturally falls under main sections.
- Organize content in a hierarchy matching the site's structure, with subcategories where needed.
- Keep categories broad and easy to explain.
- Use tags, not categories, for fine details.
- Avoid overlapping categories that make placement ambiguous.
- Why: Clear, broad boundaries let users predict what they'll find and where.

## 82. Cards
- Problem: Users browse a collection mixing content types and lengths.
- Use when: Users browse rather than search, and content mixes images, video, and text.
- Show each entry as a similarly shaped card with a short summary and clear action.
- Scroll the collection in one direction only.
- Truncate overflow with an expand option; never scroll inside a card.
- Keep one subject per card and few actions.
- Don't use cards for uniform lists, galleries, or strictly ordered content.
- Why: Cards chunk content into familiar, scannable units that adapt across screen sizes.

## 83. Carousel
- Problem: Users browse a set of items and may select one.
- Use when: Items are highly visual and space is limited, and you want to hint at more.
- Show items in a horizontal row with thumbnails, about 3 to 8 visible at once.
- Provide arrow controls and animate the chosen item into focus.
- Loop from end to start.
- Don't use it for non-visual items that an image cannot identify.
- Why: It saves space and teases hidden content to encourage exploration.

## 84. Progressive disclosure
- Problem: Too much information or too many options at once overwhelm users.
- Use when: Content volume or choice count may overload users.
- Show only what the current task needs.
- Move advanced or rarely used options to a secondary view.
- Provide "Show more" or similar for deeper detail.
- Keep completed steps visible so earlier input can be revised.
- Never hide essential information or the next action.
- Why: Revealing detail on demand cuts clutter and cognitive load and makes the product easier to learn.

## 85. Continuous scrolling (infinite scroll)
- Problem: Large datasets don't fit one page and users want to browse uninterrupted.
- Use when: There is more content than a page can hold and leaving the page would break flow.
- Load the next batch automatically as the user nears the end and append it.
- Show a loading indicator.
- Don't use it for predictable or alphabetical lists or when users need to jump to a spot; use pagination.
- Keep footers reachable (reserve space, back-to-top link, fixed header).
- Why: It removes "next page" friction but obscures the end and makes returning to a position harder.

## 86. Tag cloud
- Problem: Users want to browse by popularity in an engaging way.
- Use when: Users add their own tags and there are more than about 10 to 20 tags with varying counts.
- Size each tag by its weight.
- Pick one clear weight measure.
- Order alphabetically, randomly, by weight, or in related clusters.
- Don't use it for strict hierarchical categories.
- Why: It shows at a glance which topics dominate and what the site covers.

## 87. Event calendar
- Problem: Users need to find events in a time period, presented for easy scanning.
- Use when: Items are tied to dates or times.
- Group events into human time buckets (tonight, next week, next month).
- Show more detail for near events; optimize distant ones for scanning and filtering.
- Always show start times.
- Pair any boxed month grid with a text list of details.
- Group and filter by how users think, not internal categories.
- Why: People plan in loose chunks of time, and dated items are easy to group and filter.

## 88. Archive
- Problem: Collection items must be arranged in time order for finding and following.
- Use when: More than 10 to 20 items span a long period.
- Sort chronologically with headings sized to volume.
- Don't split into small periods that hold only a few items; don't list empty periods.
- Link each period to its own page or list items directly.
- Why: Archives let users trace how content evolved over time.

## 89. Thumbnail
- Problem: Users want to scan many images without loading full-size files.
- Use when: Presenting collections of images, videos, or pages.
- Show a small preview of each item.
- Use the same width and height for all thumbnails in a set.
- Resize and crop to preserve proportions; a medium default (around 80x80 px) is a good start.
- Don't let thumbnails vary in size within a grid.
- Why: Previews let users browse many items on one page and choose without clicking through.

## 90. Favorites
- Problem: Users want to set aside items to revisit.
- Use when: There's a large volume of content; use tags or categories for grouping instead.
- Add a star or heart toggle in lists and detail views.
- Give users a personal list of saved items.
- Keep favoriting a simple on/off toggle.
- Don't conflate favorites with likes or shares; it's personal curation.
- Optionally allow notes or tags for recall.
- Why: Favorites help people separate what they care about from overwhelming volume.

### Group: Gestures

## 91. Pull to refresh
- Problem: Users need a way to load newer content or refresh the view.
- Use when: Updating reverse-chronological lists (feeds, inboxes) on touch screens.
- Reveal a refresh indicator at the top as the user pulls down.
- Cancel if released before the threshold.
- Keep the indicator active until new content is visible.
- Trigger it only from the user's gesture, not background sync.
- Don't rely on the gesture alone for maps, oldest-first lists, galleries, or fast-changing data; offer a visible refresh button or auto-update.
- Why: It gives manual control and context, but hidden gestures are less discoverable than buttons.

# Part 4 — Dealing with data

### Group: Tables

## 92. Table filter
- Problem: Users need to narrow a large table to rows matching column categories.
- Use when: Results exceed one page and one or more columns group into categories.
- Provide dropdowns listing each filterable column's categories.
- Show only matching rows when the filter is applied; allow multiple filters.
- Update each dropdown's options as other selections narrow them, so users can't pick empty combinations.
- Don't filter on columns whose values can't be sensibly grouped.
- Why: Fewer visible rows lead users to more accurate results.

## 93. Alternating row colors
- Problem: Users lose track of which values belong to which row when scanning similar rows.
- Use when: Tables have many similar columns, multi-line rows, or varying row heights.
- Shade every second row with a slightly different background.
- Keep both shades close in lightness and low in saturation; one can be the page background.
- Avoid strong contrast that competes with the data.
- Why: Subtle striping helps the eye follow a row across columns.

## 94. Sort by column
- Problem: Users need to reorder rows by a column's values to compare items.
- Use when: Tables have more than about 10 rows, span pages, or hold comparable values.
- Make each column header clickable.
- Sort ascending on first click; reverse on repeat click.
- Show a direction arrow beside the active header and style it distinctly.
- Don't add sorting to tiny, easily scanned tables.
- Why: It's a familiar desktop convention for organizing and comparing data.

### Group: Formatting data

## 95. Frequently asked questions (FAQ)
- Problem: Users have recurring questions about a site and its services.
- Use when: Support and feedback channels show common shared concerns.
- Maintain FAQs in a dedicated, regularly updated section.
- Group questions into logical categories (validate with card sorting).
- Put the most frequent questions first.
- Keep questions short, scannable, searchable, and in users' own wording.
- Don't let styling overwhelm content; always offer a way to ask a new question.
- Why: Users quickly find answers that fit their situation, with a clear next step.

## 96. Dashboard
- Problem: Users need to absorb data from several sources at a glance.
- Use when: A high-level overview should make actionable trends easy to spot.
- Build around one clear goal and include only data serving it.
- Put the most urgent metrics at the top, secondary stats lower.
- Separate operational, strategic, and analytical needs into different views.
- Offer drill-down for detail.
- Don't overload the screen with unrelated data or decoration.
- Why: Focused dashboards enable fast, informed decisions.

## 97. Copy box
- Problem: Users need to view and copy preformatted text such as code without losing layout.
- Use when: Showing monospaced or code-like content meant to be pasted elsewhere.
- Style the block distinctly (font, color, background).
- Use a monospace font so indentation holds.
- Preserve whitespace with preformatted or textarea markup.
- Don't use it for regular body text.
- Why: Browsers collapse whitespace, so preformatting keeps text readable and copyable.

### Group: Images

## 98. Gallery
- Problem: Users browse a collection of high-quality images.
- Use when: Users move through images in sequence and need maximum space for each.
- Show one image at a time with previous/next controls and keyboard arrows.
- Show position (for example "2 of 18").
- Provide thumbnails or numbered tabs for jumping, highlighting the current one.
- Update only the image, caption, and context, not the whole page.
- Use a grid instead when users need an overview of many images at once.
- Why: Position cues and multiple navigation routes keep users oriented, and partial updates feel fast.

## 99. Slideshow
- Problem: Several media items must share one limited space.
- Use when: Highlighting several stories in one spot for skimming; not when all must be visible.
- Rotate slides automatically at intervals with a simple slide or fade.
- Show indicators of slide count and position.
- Label each slide's button with a specific action, not "Read more".
- Reveal previous/next controls on hover.
- Don't combine with other animations or use for minor stories.
- Why: It packs highlights into one area, but overuse makes pages feel busy.

## 100. Image zoom
- Problem: Users need fine detail that the default image size can't show.
- Use when: Full-resolution images would slow loading or break layout.
- Trigger zoom on click or hover and load high-res only then.
- Add a visible cue (icon, text) that zoom exists.
- Don't preload high-res for every image.
- Show detail in a zoom area or modal while keeping the overview visible; don't zoom so far users lose their place.
- Why: Users examine details without losing context or wasting bandwidth.

### Group: Search

## 101. Autocomplete
- Problem: Users struggle to search for things they can't recall exactly or might mistype.
- Use when: The dataset is manageable, speed and accuracy matter, and the list is too big for a dropdown.
- Pair a labeled text field with suggestions that update as the user types.
- Support keyboard, touch, and mouse selection.
- Rank by relevance, cap at about 10 suggestions, and highlight the matching part.
- Let Esc close the list and typing reopen it; don't use it as an overview of all options.
- Why: Recognition beats recall, cutting keystrokes and errors.

## 102. Search filters (live filter)
- Problem: Users must narrow many results using contextual categories.
- Use when: Results are numerous and categorizable.
- Show all results first, then let users remove unwanted ones via filters.
- Offer filters as text fields, dropdowns, checkboxes, or radios.
- Update results instantly on each change.
- Don't use it if content can't be meaningfully categorized or if filters complicate rather than simplify.
- Why: Searching becomes an interactive dialogue with immediate feedback.

# Part 5 — Social

### Group: Reputation

## 103. Testimonials
- Problem: Visitors need outside proof before trusting a product's claims (the site's problem field is blank; inferred).
- Use when: You need credibility for your value claims.
- Show statements from real, satisfied customers.
- Add a photo, name, or video to increase believability.
- Place testimonials next to the claims they support.
- Avoid vague, unattributed praise.
- Why: People trust peer reviews nearly as much as personal recommendations.

## 104. Leaderboard
- Problem: Users want to know who the top performers are.
- Use when: The community and its activities are genuinely competitive; avoid it for writing, feedback, or photo sharing.
- Show a fixed number of ranked competitors.
- Offer time-period and category views, defaulting to daily or weekly so ranks stay fresh.
- Show the user's own rank with neighbors directly above and below.
- Compare users of similar activity; consider friends-only boards.
- Update continuously and expect gaming.
- Why: Comparison motivates competitors but can entrench elites and discourage newcomers.

## 105. Collectible achievements
- Problem: Visible awards motivate some users and can raise engagement.
- Use when: Guiding users to features or offering status within a community.
- Reward specific behaviors your community values, not raw activity.
- Build a consistent set including specialized awards so different users can excel.
- Make awards attractive and easy to display.
- Mix easy early wins with harder, progressively unlocked challenges.
- Don't reward repetitive or low-quality activity, and check for antisocial incentives.
- Why: Awards signal reputation and history, building ownership and belonging.

### Group: Social interactions

## 106. Activity stream
- Problem: Users want a quick overview of recent relevant actions.
- Use when: User activity is central to the product.
- Merge recent actions of contacts and followed accounts into one live feed.
- Use a consistent layout per activity type with a prominent avatar.
- Collapse repeated similar actions into one story.
- Link each item to the actor, the subject, and the activity.
- Omit negative actions (dislikes, unfriending).
- Why: Seeing others' activity invites participation and keeps content timely.

## 107. Auto-sharing
- Problem: Users want easy ways to post their activity to social networks.
- Use when: Sharing is a natural part of the flow.
- Build sharing into the action itself.
- Provide granular settings for which activities are posted.
- Publish in-app and to external networks.
- Never auto-share personal or sensitive content.
- Why: It removes a step users would take anyway and spreads awareness.

## 108. Friend list
- Problem: Users want to track and engage with a smaller group of friends.
- Use when: Users should explore members, find contacts, or choose who sees their content.
- Show connections in a scannable list linked to profiles.
- Pair with a follow option where useful.
- Don't dump huge unfiltered lists.
- Make audience/sharing controls clear.
- Why: Seeing known people's activity keeps users engaged and gives control over audience.

## 109. Chat (direct messaging)
- Problem: Users need private communication with individuals or groups.
- Use when: Users should contact each other directly.
- Provide an inbox of recent messages and a sent view.
- Provide a compose form with a clear send action.
- Support one-to-one and group conversations.
- Why: Messaging is a core interface that supports everything from transactions to relationships.

## 110. Invite friends
- Problem: Users want to use the product with their friends.
- Use when: The product is more valuable with others.
- Keep the invite flow short.
- Offer contact import and a shareable link.
- Place invites in onboarding or empty states.
- Don't make invites hard to find or complicated.
- Why: People respond more readily to friends than strangers, and shared use deepens engagement.

## 111. Friend
- Problem: Users want a mutual, personal connection with another person.
- Use when: Users should build a closed circle for sharing.
- Require both sides to agree; keep the link two-way.
- Unlock shared actions only after acceptance.
- Show connection status and allow undoing.
- Never connect people automatically.
- Why: Mutual consent creates a closer bond than one-way following.

## 112. Follow
- Problem: Users want updates on topics or themes, not only people.
- Use when: Users should personalize around subjects they care about.
- Let users follow topics, channels, events, interests, or people.
- Show followed items in a central feed.
- Use follows to suggest related items.
- Don't require mutual connection or that friends use the app.
- Why: Users get varied content independent of their friends' tastes.

## 113. Reaction
- Problem: Users want a quick, low-effort way to show how they feel.
- Use when: Informal feedback is enough.
- Offer one-tap emotional responses instead of star ratings.
- Treat each as a simple yes/no signal.
- Aggregate reactions to surface interesting content.
- Keep the option count small.
- Why: Dropping fine-grained rating makes feedback easy to give and interpret.

# Part 6 — Miscellaneous

### Group: Shopping

## 114. Coupon
- Problem: Users need an incentive to buy.
- Use when: Highlighting an offer, rewarding commitment, or targeting a segment.
- Provide a field for entering a coupon code.
- Offer percentage or fixed discounts, free shipping, or gifts.
- Issue separate codes per channel or audience to track sources.
- Show clearly how the code changes the total.
- Don't make shoppers without a code feel they're missing out, and don't hide the final price.
- Why: Time-limited offers feel like losable gains and prompt action; codes make campaigns measurable.

## 115. Pricing table
- Problem: Users need a clear comparison of plans, features, and prices.
- Use when: The product comes in several versions.
- Line up each plan's price with its features in a table.
- Visually separate plans and emphasize the recommended one.
- Make titles and prices stand out with size and color.
- Repeat prices at top and bottom, or keep the table short.
- Add an FAQ below (free plan, refunds, billing).
- Why: Side-by-side comparison shows capability and encourages upgrades.

## 116. Product page
- Problem: Shoppers need product details to decide, and key info is often hard to find.
- Use when: Presenting a physical product for sale.
- Always show name, main image, price, and a clear buy button.
- Add variants, stock, delivery time, quantity, zoom, and specs only when they help.
- Group related information and link related products.
- Use quality photos and video from many angles.
- Add reviews and trust signals; never hide key details.
- Why: Clear, trustworthy details convert interest into purchase.

## 117. Shopping cart
- Problem: Shoppers need a familiar way to gather products before paying.
- Use when: Customers may buy several items or return later.
- Let users add, remove, and change quantities.
- Show per-item subtotals plus shipping, tax, and fees.
- Put add-to-cart beside every product.
- Keep the cart viewable at all times, with continue-shopping and checkout options.
- Don't use a cart for single-product sales.
- Why: The cart metaphor signals nothing is bought until checkout.

### Group: Increasing frequency

## 118. Tip a friend
- Problem: Users want to share something with a peer.
- Use when: Content is hard to pass on by copy-paste.
- Place a share link near the content.
- Collect sender details and a short personal message.
- Send a clean condensed version or a link.
- Safeguard against arbitrary recipients to prevent spam abuse.
- Why: Formatted sharing is easier, but the feature is spam-prone and rarely used.

# Part 7 — Persuasive patterns - Cognition

Persuasive patterns are summarized as design principles. Each has an "Ethical caution" line: where the site gave one it is paraphrased; otherwise the caution is our own guidance (marked "[added]"). General rule for this whole part: use these effects to help users reach goals they themselves hold, never to extract choices they would reject on reflection; any scarcity, social proof, or deadline you show must be true.

### Group: Loss aversion

## 119. Status-quo bias
- Problem: People tend to keep the default or current option instead of weighing real costs and benefits.
- Use when: You want a particular default adopted or need to retain customers through a change.
- Preselect the option that best serves most users.
- Limit the number of choices to avoid stalling.
- Frame the recommended option as the baseline (for example, a new plan presented as the current plan plus extras).
- To encourage change, show the cost of staying alongside the gains of switching.
- Why: Under complexity or uncertainty people fall back on keeping what they have.
- Ethical caution: The site cites a privacy-settings change that relied on an opaque opt-out default. [added] Never default users into data sharing, paid add-ons, or consent; defaults must be the choice a well-informed user would make.

## 120. Optimism bias
- Problem: People overestimate their chances of success and underestimate risks.
- Use when: You want users to set realistic goals or take risks seriously.
- Make the risks of critical actions explicit and offer a safer alternative.
- Prompt a pessimistic view first (pre-mortem, "imagine this failed").
- Show both positive and negative future scenarios.
- Why: People expect best-case outcomes and discount conflicting evidence.
- Ethical caution: The bias causes harm by making people update beliefs selectively; [added] use the principle to correct over-optimism, not to exploit it (for example in lending, gambling, or trial sign-ups).

## 121. Framing
- Problem: How a fact is presented changes the judgment people make about it.
- Use when: Decisions rest on factual evidence you present.
- Choose deliberately between gain and loss framing ("90% lean" vs. "10% fat").
- Give figures a reference point (industry average, competitor).
- Frame offers as protecting something the user has.
- Why: People are risk-averse for gains and risk-seeking for losses, and judge value relative to a comparison.
- Ethical caution: [added] Framing must not distort the underlying fact; show the plain number too when stakes are high (health, money).

## 122. IKEA effect
- Problem: People value what they helped create far more than identical things they didn't.
- Use when: You want higher satisfaction through participation or want users to stick with a project.
- Let users assemble or customize part of the product.
- Keep the tasks achievable; start with light customization.
- Expect change aversion around things users invested in.
- Why: Completing effortful work brings competence and ownership; the value vanishes if the creation is destroyed.
- Ethical caution: The site notes the same effect makes people cling to failing projects; [added] don't require busywork purely to raise switching costs.

## 123. Decoy effect
- Problem: An extra, deliberately inferior option shifts which option people choose.
- Use when: You want one option to look more attractive or to change the criteria users weigh.
- Make the decoy worse than the target on every attribute.
- Make the competitor better than the decoy on only some attributes.
- Let the target clearly dominate the decoy.
- Why: Decoys ease choice overload and give people a rationale for an intuitive pick.
- Ethical caution: The site notes decoys work largely unconsciously; [added] that is why they are manipulative when used to upsell; prefer honest comparison and a genuine recommendation.

## 124. Loss aversion
- Problem: Losses feel stronger than equal gains, so gain-framed choices are often resisted.
- Use when: A choice can be framed as gain or loss and you want users to start or continue.
- Frame around what users would forfeit by leaving.
- Offer trials so stopping feels like waste of invested time.
- Fix problems immediately (replace faulty items fast).
- Split good news into several small wins.
- Why: Losses weigh roughly twice as much as gains.
- Ethical caution: [added] Don't threaten loss of user data or fabricate losses to block cancellation; letting users export and leave cleanly is required.

## 125. Sunk cost effect
- Problem: People keep investing in something because of what they already spent.
- Use when: Raising usage, upgrades, or add-ons after a sale.
- Offer upgrades to already-committed subscribers.
- Encourage use of paid services.
- Send reminders before booked events highlighting their value.
- Offer check-ups on durable goods.
- Why: Abandoning a past investment feels like a loss.
- Ethical caution: The site advises making the bias visible so people can weigh real costs vs. benefits. [added] Never use it to keep users paying for something that no longer helps them.

## 126. Endowment effect
- Problem: People value things more once they feel they own them.
- Use when: You want to retain users or make them prefer your product.
- Let users build ownership (saved items, wish lists, profiles, ratings).
- Use trials or invested time to create ownership.
- Show what users have accumulated.
- Make accumulated data feel personal.
- Why: Owned things become the baseline, so losing them hurts more than an equal gain pleases.
- Ethical caution: [added] Ownership must be real: let users export what they built; never hold data hostage.

## 127. Negativity bias
- Problem: Negative experiences and information weigh more than positive ones.
- Use when: Anticipating bad moments or framing messages.
- Separate positive messages from negative ones so the positive aren't drowned out.
- Bundle several negative messages into one.
- Pair bad news with a quick, easy fix.
- Map emotional highs and lows of the journey and address confusion early.
- Why: Negative events have stronger, longer-lasting psychological pull.
- Ethical caution: [added] Don't use fear or negative framing to pressure decisions; be honest about problems.

### Group: Other cognitive biases

## 128. Illusion of control
- Problem: People believe they control outcomes that are actually beyond their reach.
- Use when: Motivating users toward a goal.
- Give users real control over their actions.
- Show clearly how actions affect progress.
- Keep expectations realistic and don't overstate influence.
- Why: Feeling in control builds confidence and drive.
- Ethical caution: The site warns illusory control can encourage unsafe behavior, risk-taking, and poor learning; [added] never use it in chance-based or financial contexts to suggest skill where there is none.

## 129. Set completion
- Problem: People are driven to collect every item of a set as they near completing it.
- Use when: Motivating a series of actions or exploration of a product.
- Group items into logical sets.
- Size sets to be finishable, slightly beyond typical completion.
- Create multiple levels of sets.
- Celebrate completion and suggest next paths.
- Why: Finishing a set satisfies; unfinished sets nag.
- Ethical caution: [added] Don't attach completion to paid random items (loot-box mechanics) or endless sets.

## 130. Present bias
- Problem: Immediate wants conflict with long-term goals.
- Use when: Leveraging the pull of instant rewards, or helping users separate present and future selves.
- Let users decide in advance (pre-commitment, order ahead).
- Prioritize near-term benefits.
- Time-limited offers increase impulse buying (use carefully).
- Why: Perceived value of future rewards drops steeply with delay (hyperbolic discounting).
- Ethical caution: [added] Prefer the pre-commitment use that serves users' own long-term goals; avoid engineering impulse purchases.

## 131. Delay discounting
- Problem: People prefer smaller, sooner rewards to larger, later ones.
- Use when: Prompting action now or breaking a big conversion into small immediate rewards.
- Lead with value available now.
- Offer small immediate perks over larger delayed ones.
- Keep waits short.
- Deferred payment makes cost feel distant.
- Why: Reward value shrinks as waiting grows.
- Ethical caution: [added] "Pay later" mechanics can drive debt; disclose total cost clearly and avoid targeting vulnerable users.

## 132. Need for closure
- Problem: People prefer a definite answer to lingering uncertainty.
- Use when: Motivating action via small wins; not for burdensome, long-term goals.
- Offer small tasks or sets leading to a complete state.
- Surface unfinished items with an easy resolution.
- Make steps to completion clear and simple.
- Why: Unresolved goals create tension people want to relieve, and can make them settle on early cues.
- Ethical caution: [added] Don't manufacture open loops (fake unread badges) to pull users back.

## 133. Curiosity
- Problem: Partial information makes people want the rest.
- Use when: Moving people toward an action or converting visitors to leads.
- Reveal just enough to spark interest and give a clear next step.
- Use surprise to hold attention.
- Release information gradually across touchpoints.
- Let users explore and discover.
- Why: A knowledge gap creates a drive to close it.
- Ethical caution: The site warns against adding so much discomfort that it becomes a problem; [added] avoid clickbait that the payoff doesn't honor.

## 134. Priming effect
- Problem: Recent exposure quietly steers later decisions.
- Use when: Nudging a choice or setting an emotional tone for a later decision.
- Use metaphors that evoke the desired outcome.
- Evoke relevant feelings with imagery or video.
- Use colors and images that cue ideas recalled later.
- Why: Prior exposure makes related ideas faster and more fluent to process, and fluency feels like preference.
- Ethical caution: The site notes that the robustness of much priming research has been questioned. [added] Don't build on it as a reliable lever, and never use it to bypass informed consent.

## 135. Value attribution
- Problem: People judge value from surface cues (price, looks, brand) rather than real merit.
- Use when: Raising perceived value or differentiating.
- Make core distinctive traits stand out (premium tier, distinct brand).
- Let users invest time before asking them to pay.
- Ask when perceived value peaks.
- Why: People infer hidden qualities from a few visible cues.
- Ethical caution: [added] Perceived value should track actual value; don't inflate price or polish to mask a weak product.

## 136. Peak-end rule
- Problem: Experiences are remembered mainly by their most intense moment and their end.
- Use when: Shaping what users remember or softening losses.
- Research the highs and lows of the journey.
- Make peaks and endings positive (accomplishment, small surprises).
- Map emotions over time and fix weak spots.
- Extend the ending with follow-up care.
- Why: Emotional and final moments are encoded more vividly.
- Ethical caution: [added] A pleasant ending must not be used to paper over a painful process; fix the middle too.

## 137. Cashless effect
- Problem: People spend more when payment feels intangible.
- Use when: Increasing sales, or helping users avoid overspending.
- Make payment low-friction.
- Plan for overspenders and weigh that risk.
- Offer budgets or spending limits.
- Add friction to large purchases.
- Why: Cash makes cost visible; cards and stored credit dull that pain.
- Ethical caution: The site states customers can overspend into debt and designers bear responsibility. [added] Show real-currency prices, not opaque tokens.

## 138. Temptation bundling
- Problem: People avoid worthwhile but unpleasant tasks.
- Use when: Users need to do things they should but don't want to.
- Pair an enjoyable activity with an effortful beneficial one.
- Tie access to desirable content to the target context (for example the gym).
- Add meaningful perks to tedious routines.
- Choose sustainable rewards.
- Why: External reward supplies motivation when intrinsic drive is lacking.
- Ethical caution: [added] Serve the user's stated goal; don't use it to tie unrelated purchases together.

## 139. Inaction inertia effect
- Problem: After missing a better deal, people are less willing to accept a lesser one.
- Use when: Planning promotions so short-term discounts don't hurt later sales.
- Give every discount a clear reason and end.
- Vary each offer's form (season, size, bundle).
- Make successive offers hard to compare purely on price.
- Avoid repeated price cuts that reset the baseline.
- Why: The missed offer anchors expectations and feels like a loss.
- Ethical caution: [added] Making offers deliberately incomparable can confuse buyers; keep the actual price transparent.

## 140. Choice closure
- Problem: Decisions without a sense of finality feel less satisfying.
- Use when: Boosting post-purchase satisfaction or easing choice overload.
- Separate browsing from checkout so purchase feels closed.
- Give a closing act (close the menu, box the item).
- Add a small celebratory touch after big purchases.
- When options overwhelm, guide, then let users perform the closing act.
- Why: Physical acts that symbolize closure make decisions feel final.
- Ethical caution: [added] Closure must not prevent legitimate returns or reconsideration.

### Group: Scarcity

## 141. Limited choice
- Problem: People decide more readily when fewer options are offered.
- Use when: You want a decision now, are guiding a funnel, or reducing complexity.
- Cut options to those truly necessary.
- Find the sweet spot between too few and overload.
- Present the more complex choices first.
- Prevent analysis paralysis, especially under time pressure.
- Why: Limited processing capacity makes many similar options exhausting; smaller sets raise satisfaction.
- Ethical caution: [added] Don't hide better-for-the-user options to steer choice.

## 142. Scarcity
- Problem: Things seem more valuable when limited or hard to get.
- Use when: Signalling exclusivity or urgency.
- Show limited stock or seats remaining.
- Use deadlines or time-limited offers.
- Restrict access via invitations or caps.
- Why: Scarcity is a quality heuristic and losing an option feels bad, so people decide faster.
- Ethical caution: [added] Only show scarcity that is real and accurate; fake stock counts or "X people viewing" are deceptive dark patterns and may be illegal.

## 143. Limited duration
- Problem: Users postpone decisions without a reason to act now.
- Use when: Prompting a decision within a window.
- Set a firm end date or time limit.
- Show remaining time clearly.
- Keep the deadline consistent so it is genuine.
- Why: Time-bound opportunities trigger fear of loss.
- Ethical caution: [added] Never use fake or resetting countdown timers; real deadlines only.

# Part 8 — Persuasive patterns - Game mechanics

### Group: Gameplay design

## 144. Appropriate challenge
- Problem: Users stay engaged only when tasks are neither too hard nor too easy.
- Use when: Serving both novices and experts, or tasks cause stress or boredom.
- Hide advanced options from beginners so they get quick wins.
- Surface shortcuts and expert modes as skill grows.
- Sequence tasks to demand increasing skill.
- Raise challenge as mastery sets in.
- Why: Flow occurs when difficulty matches skill; mismatch causes anxiety or boredom.
- Ethical caution: [added] Don't artificially make tasks hard to sell shortcuts.

## 145. Storytelling
- Problem: Users don't connect with a product's purpose or journey.
- Use when: You want users engaged in a purpose or journey (implied by the site).
- Cast the user as hero and obstacles as antagonists.
- Give users an active role.
- Split the journey into episodes ending in milestones, rising in difficulty.
- Fit the product into an existing narrative.
- Why: People make decisions through stories, which lend routine tasks meaning.
- Ethical caution: [added] Stories must not misrepresent facts about the product or the user's situation.

## 146. Intentional gaps
- Problem: Users need a reason to act; deliberate incompleteness invites completion.
- Use when: Showing how an action fits a bigger picture or making the next choice obvious.
- Leave deliberate blanks users want to fill.
- Word forms as sentences to complete.
- Provide a foundation for users to finish their own way.
- Why: Incompleteness creates discomfort that motivates closure.
- Ethical caution: [added] Don't fake incompleteness (for example a profile shown as "80%" to extract unnecessary personal data).

## 147. Investment loops
- Problem: Users need a reason to invest effort now for a later reward.
- Use when: Building habit-forming, return-driven products.
- Let users invest time, data, money, or effort.
- Choose the simplest action that sets up a later reward.
- Make each loop store value so the product improves with use.
- Plan external triggers to bring users in and internal triggers to bring them back.
- Why: Anticipated reward plus prior investment drives return.
- Ethical caution: [added] Habit loops can become compulsive; measure user benefit, not just retention, and avoid them for vulnerable groups.

## 148. Periodic events
- Problem: Sustaining interest and belonging over time is hard.
- Use when: You want users returning repeatedly.
- Create a regular ritual (weekly tips, monthly report).
- Make it shared so users experience it together.
- Give each event a narrative and a next step.
- Why: Anticipation of scheduled events motivates and breaks routines.
- Ethical caution: [added] Don't use event FOMO to pressure purchases.

## 149. Hedonic adaptation
- Problem: Happiness returns to baseline after big positive or negative events.
- Use when: Extending enjoyment or releasing content gradually.
- Split experiences into smaller parts.
- Keep users mildly wanting more.
- Release content in stages to build anticipation.
- Why: Expectations adapt, so rationed pleasure feels more rewarding.
- Ethical caution: [added] Don't withhold content users already paid for to stretch engagement.

## 150. Levels
- Problem: Rising skill makes fixed difficulty boring or overwhelming.
- Use when: Matching challenge to skill or staging a complex journey.
- Split the system into levels of rising difficulty, power, and features.
- Introduce advanced functionality via progressive disclosure.
- Let users choose difficulty or unlock modes.
- Reward small milestones.
- Why: Matched challenge sustains flow and accomplishment.
- Ethical caution: [added] Don't gate basic functionality behind levels purely to drive engagement.

## 151. Self-monitoring
- Problem: Users find it hard to track the behavior they want to change.
- Use when: Helping users steer toward their own goals.
- Make measuring and tracking effortless.
- Give real-time feedback for course correction.
- Combine data with context to draw conclusions.
- Why: Seeing progress sustains motivation for things people already want to do.
- Ethical caution: The site notes tracking can make an activity less enjoyable. [added] Handle tracking data with strict privacy.

### Group: Fundamentals of rewards

## 152. Variable rewards
- Problem: Predictable rewards lose their pull.
- Use when: Users habituate to steady rewards.
- Randomize amount or timing around a consistent average.
- Avoid abruptly ending recurring rewards.
- Track rewards and pace them to avoid satiation.
- Reward activities that are enjoyable for their own sake.
- Why: Unpredictable timing sustains anticipation.
- Ethical caution: The site warns ending rewards feels like punishment. [added] Variable-ratio schedules underpin gambling and compulsive use; never combine with paid chance mechanics or minors.

## 153. Fixed rewards
- Problem: Users need motivation to start or continue desired actions.
- Use when: Rewards should follow clear goals rather than chance.
- Give a predictable reward when a clear goal is met.
- Choose rewards users understand and value (points, badges, unlocks, space).
- Tune timing and amount by iteration.
- Connect rewards into a larger progression.
- Why: Visible targets reinforce behavior.
- Ethical caution: [added] Reward behavior that benefits users, not only metrics.

## 154. Shaping
- Problem: A target behavior feels too daunting to do all at once.
- Use when: Desired behavior is complex or intimidating.
- Split it into small steps.
- Reward early rough approximations.
- Raise the bar gradually.
- Eventually reward only the full target behavior.
- Why: Reinforcing successive approximations builds complex behavior (operant conditioning).
- Ethical caution: [added] Be transparent about where the steps lead.

### Group: Gameplay rewards

## 155. Goal-gradient effect (completion)
- Problem: Motivation drops when a goal feels far and rises as it nears.
- Use when: Guiding users to an end goal or marking stage ends.
- Break large tasks into rewarded steps.
- Set clear expectations and show how far along users are.
- Make completion official (badge, certificate).
- Give a head start (pre-filled progress, a partly stamped card: endowed progress).
- Why: Nearby rewards motivate more, and progress accelerates action.
- Ethical caution: [added] Head-start progress must reflect real work done, not invented credit used to lock users in.

## 156. Privileges (powers)
- Problem: Users want faster ways to reach their goals.
- Use when: Users have natural roles or you reward quality contributions.
- Let users earn abilities that speed their goals.
- Reward contributors and curators.
- Give trusted users extras (weighted votes, moderation rights).
- Grant perks temporarily or permanently.
- Why: Influence and capability meet needs for competence, relatedness, and autonomy.
- Ethical caution: [added] Watch for power concentration and abuse; provide accountability.

## 157. Unlock features
- Problem: Rewards that don't keep pace with skill lose interest.
- Use when: Separating newcomers from veterans or guiding exploration.
- Unlock tools and challenges as experience grows.
- Tie unlocks to points or milestones.
- Show unlocked features so newcomers have aims.
- Why: Effort invested increases valued membership and signals trust.
- Ethical caution: The site warns points can be gamed, push out newcomers, lose excitement, and that removing features for inactivity drives users away.

## 158. Delighters
- Problem: People remember unexpected, playful experiences.
- Use when: Standing out or making experiences memorable.
- Add playful microcopy, fun visuals, friendly compliments.
- Hide small surprises to discover.
- Keep novelty moderate.
- Use surprise to counter habituation.
- Why: Novelty counters habituation and raises recall and word of mouth.
- Ethical caution: [added] Delight must not distract from important information or consent.

## 159. Achievements
- Problem: People engage most when accomplishments earn recognition.
- Use when: Showing what's achievable and letting users track and compare progress.
- Map achievable goals to desired behaviors.
- Split big goals into skill-matched wins.
- Publish achievements with progress indicators.
- Show what similar peers accomplished.
- Why: Achievements anchor expectations and trigger social comparison and commitment.
- Ethical caution: [added] Avoid shaming users who don't achieve; make public display opt-in.

## 160. Praise
- Problem: Users can't tell if they did the right thing.
- Use when: Directing correct behavior or keeping users moving.
- Identify desired-action moments.
- Respond with a message, visual, or sound.
- Match praise to what the user tried to do.
- Use it sparingly so it stays meaningful.
- Why: Positive feedback reinforces behavior.
- Ethical caution: [added] Don't praise actions that mainly benefit the business (for example sharing contacts).

## 161. Appointment dynamic
- Problem: Getting users to return at set times to act and collect rewards.
- Use when: Building repeat-visit habits.
- Use a recurring, memorable cadence.
- Make the window, reward, and consequences clear.
- Tell users when to return next.
- Ask small commitments first, bigger later.
- Why: Visible deadlines create urgency and commitment.
- Ethical caution: [added] Punishing missed appointments (decaying crops, lost streaks) can create anxiety; keep penalties mild.

## 162. Prolonged play
- Problem: Users need reasons to keep playing and improving.
- Use when: Motivating referrals or engagement by granting more time or resources.
- Identify the core resource (storage, quotas, slots).
- Set easy, clearly stated goals.
- Reward goal achievement by extending the resource.
- Mix in other reward types.
- Why: Extending a valuable resource feels like security and reinforces behavior.
- Ethical caution: [added] Referral-for-resource schemes should not pressure users to spam contacts.

# Part 9 — Persuasive patterns - Perception and memory

### Group: Attention

## 163. Tunnelling
- Problem: Multi-step processes offer chances to influence users at each stage.
- Use when: Removing distractions once a user has decided to act.
- Remove competing menus, links, and promotions.
- Lead through a fixed sequence.
- Present relevant info in the flow.
- Preserve users' sense of control over entering the process.
- Why: Once people commit to a process, they stay consistent with it.
- Ethical caution: The site notes users surrender some self-determination to the designer's path. [added] Always provide a visible exit and don't slip in unrequested upsells.

## 164. Reduction
- Problem: Complex tasks deter users.
- Use when: Routine tasks are hard to grasp or competitors haven't simplified.
- Trim tasks and set aside rarely needed options.
- Lower effort so benefit clearly exceeds cost.
- Use sensible defaults and let users refine later.
- Base decisions on what similar users chose.
- Why: People avoid effort; simplicity increases perceived payoff and confidence.
- Ethical caution: [added] Simplification must not hide important terms or costs.

## 165. Isolation effect
- Problem: Distinctive items are remembered better than similar neighbors.
- Use when: One item should draw more attention.
- Make key information or actions visually distinct.
- Use meaningful contrast to aid comparison.
- Use sparingly.
- Explain why the item is highlighted.
- Why: Novel stimuli capture attention and memory.
- Ethical caution: [added] Don't use visual emphasis to steer users away from the option that's best for them (for example greying out "decline").

## 166. Picture superiority effect
- Problem: Pictures are remembered far better than words.
- Use when: Improving recall or attention.
- Pair key messages with relevant images.
- Use visual metaphors for complex ideas.
- Prefer faces or objects in context over empty scenes.
- Focus on a subject without losing context.
- Why: Dual coding: images plus words encode better than either alone.
- Ethical caution: [added] Images must not misrepresent the product.

## 167. Zeigarnik effect
- Problem: Unfinished tasks are remembered better than finished ones.
- Use when: Encouraging completion or exploration.
- Break experiences into small steps.
- Show progress clearly.
- Create task lists, including onboarding checklists.
- Remind users of unfinished tasks and how to complete them.
- Why: Incomplete tasks stay active in memory.
- Ethical caution: [added] Don't invent tasks that serve only the business, and limit reminder frequency.

### Group: Comprehension

## 168. Chunking
- Problem: People process and recall information better in small groups.
- Use when: Users must absorb or remember a lot; not for search or analysis.
- Group information into a few chunks.
- Split long strings (phone numbers) into segments.
- Separate headings from body.
- Auto-format inputs (expiry dates, phone numbers).
- Why: Short-term memory holds only a few units.
- Ethical caution: The site warns against misusing chunking as a justification for general simplicity or minimalism; it applies only to processing limits.

## 169. Anchoring
- Problem: People rely heavily on the first number they see.
- Use when: Making a price seem fair or shaping expectations.
- Show a reference price or offer first.
- Keep the anchor believable.
- Expect weaker effects with expert buyers.
- Why: Early numbers pull later estimates toward them.
- Ethical caution: [added] Reference prices must be real ("was" prices actually charged); fake anchors are deceptive.

## 170. Serial position effect
- Problem: Items at the start and end of a list are remembered best.
- Use when: Ordering menus or feature lists.
- Put important items first and last.
- For immediate decisions put the preferred option last; for later decisions, first.
- Show only task-relevant information.
- Add cues that aid recognition.
- Why: Early items enter long-term memory; final items stay in working memory.
- Ethical caution: [added] Don't bury important disclosures in the middle.

## 171. Recognition over recall
- Problem: Unaided recall is hard; recognition is easy.
- Use when: Learning preferences or reducing data entry effort.
- Offer predefined choices to click or rate.
- Use menus, multiple choice, autocomplete, imagery.
- Group items by category.
- Provide confirmable defaults.
- Why: Contextual cues make retrieval easier.
- Ethical caution: [added] Predefined choices shouldn't be loaded to skew answers.

## 172. Pattern recognition
- Problem: People seek order in complex information.
- Use when: Users organize or label information.
- Make sorting/labeling playful.
- Add affordance cues showing how elements work.
- Learn preferences from choices and surface fitting content.
- Why: Matching expectations reduces mental effort.
- Ethical caution: [added] Be transparent about preference learning and avoid filter bubbles.

## 173. Sequencing
- Problem: Complex tasks overwhelm and get abandoned.
- Use when: Users need help finishing complex processes.
- Split into small steps or a checklist.
- Give each step a clear objective.
- Show steps remaining.
- Cut unneeded steps and tailor later ones.
- Why: Working memory is limited.
- Ethical caution: [added] Don't hide costs until late steps (drip pricing).

## 174. Conceptual metaphor
- Problem: People grasp new ideas through familiar ones.
- Use when: Making the unfamiliar familiar.
- Frame the product through a familiar analogy.
- Explain features via known concepts.
- Mirror traits of familiar things.
- Link to familiar emotions.
- Why: Familiar associations cut the effort of understanding.
- Ethical caution: The site notes metaphor effects vary with time and culture; [added] test with your audience.

# Part 10 — Persuasive patterns - Feedback

### Group: Timing

## 175. Kairos
- Problem: Users are more receptive at certain moments.
- Use when: Timing affects receptiveness.
- Map life transitions (moving, new baby).
- Map habits and seasonal fresh starts.
- Time messages to those moments.
- Tailor to the individual's situation.
- Why: Transitions open people to change.
- Ethical caution: [added] Inferring life events from data is sensitive; don't exploit vulnerable moments (grief, illness).

## 176. Feedback loops
- Problem: People respond to clear information on how their actions are working.
- Use when: You want users to respond to feedback right away.
- Measure and show where users stand.
- Present results in meaningful context.
- Tie feedback to a larger goal with next paths.
- Give a moment to adjust, and measure that too.
- Why: Positive loops drive change, negative loops stabilize.
- Ethical caution: [added] Feedback must be accurate, not tuned to inflate engagement.

## 177. Tailoring
- Problem: One-size-fits-all options ignore differing needs.
- Use when: Content can adapt to needs, interests, or context.
- Adjust content to each user.
- Show returning users they're remembered.
- Deliver relevant info in real time.
- Use intent and situation.
- Why: Personalized content persuades better and reduces clutter.
- Ethical caution: [added] Be transparent about data used and offer opt-out.

## 178. Trigger
- Problem: Capable users who don't act need a timely prompt.
- Use when: Reminding or motivating a specific action.
- Raise motivation when ability is present but drive is low.
- Simplify the behavior when motivation exists but ability is low.
- Send a simple signal when both are high.
- Fit triggers to context, including offline.
- Why: Behavior occurs when motivation, ability, and prompt coincide (Fogg model).
- Ethical caution: [added] Respect notification limits and quiet hours; avoid fear-based motivation.

## 179. Simulation
- Problem: People struggle to see how inputs affect outcomes.
- Use when: Allowing safe experimentation.
- Show cause and effect immediately.
- Provide a low-stakes sandbox.
- Rehearse target behaviors safely.
- Model real context believably.
- Why: Seeing outcomes change in real time makes the link concrete.
- Ethical caution: [added] Simulations must be accurate, not rigged to favor a sale.

## 180. Fresh start effect
- Problem: Goals set at the start of new periods are more often pursued.
- Use when: Users need extra motivation or you're timing a call to action.
- Frame time landmarks as fresh starts.
- Use past attempts as benchmarks.
- Expect boosts to fade.
- Keep the required behavior simple.
- Why: Landmarks separate past failures from a new self.
- Ethical caution: [added] Avoid guilt about past failures.

# Part 11 — Persuasive patterns - Social

### Group: Social biases

## 181. Authority bias
- Problem: People defer to authority, often based on surface cues.
- Use when: Expert endorsements are genuine and relevant.
- Show verifiable credentials, certifications, awards, real testimonials.
- Link to relevant recognized experts.
- Establish your own authority through confident content.
- Match the authority to the audience and field.
- Why: Authority serves as a decision shortcut.
- Ethical caution: The site warns fabricated or exaggerated endorsements mislead and over-reliance discourages critical thinking; keep credentials genuine, verifiable, and current.

## 182. Liking
- Problem: People agree more readily with those they like.
- Use when: You need strangers to comply with requests.
- Make the design attractive.
- Show shared background or problems; use peer testimonials.
- Give sincere praise and encourage engagement.
- Frame cooperation against a common challenge.
- Why: Liked sources get favorable assumptions and less scrutiny.
- Ethical caution: The site warns against fake personas, undisclosed paid endorsements, and invasive over-personalization.

## 183. Retaliation
- Problem: People repay treatment in kind, fair or unfair.
- Use when: Playful competition or curating UGC; not where feuds could escalate.
- Give value before asking.
- Build trust before requesting commitment.
- Keep exchanges fair with timely acknowledgment.
- Add cooldowns, moderation, and guidelines.
- Why: Loss aversion makes slights feel heavy, prompting balancing.
- Ethical caution: The site warns of vendettas, bullying, and groupthink; require safeguards, monitoring, and appeal routes.

## 184. Role playing
- Problem: People act according to the persona they occupy.
- Use when: Changing attitudes, setting norms, or adding playful roles.
- Build communities where users can take on roles.
- Assign roles such as advocate for a position.
- Encourage users to defend a position.
- Use roles to soften opposing views.
- Why: Self-generated arguments persuade more than imposed ones (self-persuasion).
- Ethical caution: [added] Be transparent when roles are used to shift beliefs.

## 185. Self-expression
- Problem: People want to show who they are and what they think.
- Use when: Users are motivated to signal identity.
- Allow personalization and sharing of content, comments, emoji.
- Add supportive feedback.
- Showcase standout creations.
- Why: Self-expression is a basic social drive.
- Ethical caution: [added] Moderate feedback to prevent harassment; respect privacy of shared content.

## 186. Reciprocation (reciprocity)
- Problem: People feel obliged to return favors.
- Use when: You can give genuine value free.
- Offer real value upfront (content, trial, early access).
- Make clear the gift carries no immediate demand.
- Make the follow-up request soon after.
- Keep the request easy and non-transactional.
- Why: Unreturned favors create discomfort.
- Ethical caution: The site warns hidden conditions and manipulative gifting erode trust; state expectations openly and let users decline without guilt.

## 187. Social proof
- Problem: People copy others when unsure.
- Use when: Visitors are new or need reassurance.
- Show the exact behavior you want, backed by others doing it.
- Place testimonials, logos, or usage stats near calls to action.
- Flag popular choices ("most popular").
- Feature people similar to the audience.
- Why: Following the majority feels safe and saves effort.
- Ethical caution: The site notes negative social proof backfires (highlighting bad behavior spreads it). [added] All numbers and testimonials must be real.

## 188. Cognitive dissonance
- Problem: When actions clash with beliefs, people adjust beliefs.
- Use when: Prompting reflection or behavior change; not for stressed or new users or safety contexts.
- Show the gap between stated goals and habits.
- Provide a clear way to close it.
- Alternate challenge with support.
- Ask small early commitments.
- Why: People seek consistency among attitudes and behavior.
- Ethical caution: The site warns overemphasis makes users feel judged and can be exploited for sales; use it only for the user's real benefit.

## 189. Positive mimicry
- Problem: People learn behavior by comparing with others.
- Use when: Teaching a behavior or building rapport.
- Reuse customers' own wording.
- Show positive actions to copy.
- Highlight good role models.
- Tailor to past choices but leave room for new things.
- Why: Mirroring creates belonging and rapport.
- Ethical caution: The site warns excessive mimicry feels creepy; be transparent, collect minimal data, offer opt-outs.

## 190. Commitment and consistency
- Problem: People want actions to match prior words.
- Use when: Users won't accept the full request upfront.
- Ask for a small voluntary commitment first.
- Break large requests into sequential steps.
- Make commitments public, personal, positive.
- Start low-stakes before purchase requests.
- Why: Committed people act consistently to avoid internal conflict.
- Ethical caution: The site stresses avoiding manipulation and seeking mutually beneficial actions; [added] avoid foot-in-the-door escalation to unwanted purchases.

## 191. Reputation
- Problem: People act to shape how others perceive them.
- Use when: Building trust, rewarding contributions, backing claims; avoid if brand reputation is negative.
- Let users build reputation through contributions.
- Show how good behavior unlocks capability and make bad behavior harder.
- Make reviews and accomplishments easy to find.
- Back claims with verifiable evidence.
- Why: Reputation is a trust shortcut under uncertainty.
- Ethical caution: The site warns against fake reviews, cherry-picking, borrowed credibility, and image laundering; let users report fake reviews.

## 192. Halo effect
- Problem: Impressions in one area spill over to others.
- Use when: Raising overall perceived quality.
- Make the first experience strong.
- Polish highly visible touchpoints.
- Leverage established brand trust for new products.
- Watch for reverse halo from bad experiences.
- Why: People seek coherent impressions.
- Ethical caution: [added] Surface polish must not conceal security or reliability weaknesses.

## 193. Nostalgia effect
- Problem: Nostalgia makes people discount costs.
- Use when: Evoking sentiment.
- Promote pro-social actions (donating, volunteering).
- Theme features around memories (throwbacks).
- Help users savor present moments.
- Why: Reminiscing shifts focus from money to social connection.
- Ethical caution: [added] Don't use nostalgia to lower users' guard on spending; resurfacing memories can be painful, so allow opt-out.

## 194. Competition
- Problem: People in shared environments strive to win scarce outcomes.
- Use when: Rallying coordinated action.
- Tap natural competitive drive.
- Make outcomes visible for comparison.
- Reward self-improvement.
- Keep recognition balanced.
- Why: Competition engages curiosity and status needs.
- Ethical caution: The site warns against over-recognizing one person at the group's expense.

## 195. Autonomy
- Problem: People want to feel in control.
- Use when: Raising satisfaction or preventing users feeling trapped.
- Make interactions fast and simple.
- Allow personalization.
- Help users feel capable and influential.
- Provide clear exits, undo, and redo.
- Why: Self-determination theory: autonomy boosts well-being.
- Ethical caution: [added] This is the counterweight to the other patterns; preserve it everywhere.

## 196. Status
- Problem: People weigh how actions affect their standing.
- Use when: Steering group behavior or rewarding good deeds.
- Give feedback on standing.
- Let users see and express status; highlight good behavior.
- Compare against others or past self.
- Allow varied roles, not a strict hierarchy.
- Why: People want to belong and conform.
- Ethical caution: The site warns not to tie status to undesirable behavior.

## 197. Noble edge effect
- Problem: Products of socially responsible companies are rated better.
- Use when: Boosting perceived quality or standing out in ambiguous markets.
- Demonstrate authentic goodwill.
- Align values with the audience.
- Emphasize goodwill in unfamiliar markets.
- Why: Goodwill spills over onto product perception.
- Ethical caution: The site says it only works when goodwill is genuine; [added] avoid greenwashing.

# Part 12 — Responsive design patterns (This Is Responsive)

## 198. Viewport baseline
- Always ship `<meta name="viewport" content="width=device-width, initial-scale=1.0">`; without it no responsive pattern works on mobile.
- Build fluid first (percentages / fr / flex), then add breakpoints only where content breaks, not per device.

## 199. Layout: Mostly Fluid
- Keep a fluid multi-column grid that just narrows; add a `max-width` container on large screens with `margin-inline: auto`.
- At the smallest breakpoint, stack columns vertically (single column).

## 200. Layout: Column Drop
- Start with all columns stacked; as width grows, place them side by side; columns "drop" below each other as width shrinks.
- Technique: `display:flex; flex-wrap:wrap` with column `flex-basis` set per breakpoint, or grid `grid-template-columns` changes inside media queries.

## 201. Layout: Layout Shifter
- Change the layout itself (not just column count) at breakpoints, e.g. sidebar left on desktop, top band on tablet, stacked on phone.
- Use CSS Grid template areas so each breakpoint re-declares `grid-template-areas` without touching HTML.

## 202. Layout: Tiny Tweaks
- For single-column pages, adjust only font-size, padding, and image size across widths; do not over-engineer breakpoints.

## 203. Layout: Main column with sidebar / 3-column variants
- Put main content first in source; on small screens show sidebar(s) below main content.
- For 3 columns: go 3 → 2 (+1 dropped below) → 1; allow content reflow so secondary columns merge.

## 204. Layout: Equal-width columns (2 to 6 up)
- Wrap N equal columns to fewer per row as width shrinks (e.g. 6 → 3 → 2 → 1).
- Technique: `grid-template-columns: repeat(auto-fit, minmax(<min>, 1fr))` gives this with zero media queries.

## 205. Layout: Off Canvas (top / left / right / left+right / bottom / full-screen overlay)
- Hide secondary panels (nav, filters) off-screen on small viewports; slide in from the relevant edge on toggle.
- Technique: `transform: translateX(-100%)` → `0` with transition; animate transform, not left/width, for performance.
- On large screens, show the panels inline instead of off-canvas.
- Full-screen overlay: cover the viewport (`position:fixed; inset:0`) and provide a clear close control.

## 206. Layout: Source-Order Shift (table-cell, flexbox, AppendAround)
- Keep HTML in the most logical/accessible order; change visual order per breakpoint.
- Technique: flex `order` or grid placement; legacy `display:table-caption/table-cell` trick; AppendAround (JS) moves a node into whichever container is visible.
- Don't let visual order diverge so much that keyboard/tab order becomes confusing.

## 207. Layout: Lists with thumbnails (+ summary)
- Small screens: small thumbnail beside or above title; hide or truncate summary.
- Wider screens: larger thumbnail and show summary text; use a media-object (image + body) flex layout.

## 208. Layout: Grid Blocks (4-up, double-wide, titled sections, equal-height, irregular)
- Reduce per-row count at breakpoints (4 → 2 → 1).
- Let feature items span two columns (`grid-column: span 2`) only when there is room; collapse to single width on small screens.
- Get equal-height rows from flex/grid stretch, not fixed heights.
- Irregular grids: use `grid-auto-flow: dense` to fill gaps.

## 209. Navigation: Toggle
- Collapse nav behind a menu button on small screens; expand inline at wider breakpoints.
- Use a real `<button aria-expanded>` for the toggle.

## 210. Navigation: Footer Anchor
- Put a "Menu" link in the header that jumps (`href="#nav"`) to the full nav in the footer; works without JS.

## 211. Navigation: Select Menu
- Convert nav into a `<select>` on small screens (low-effort, but poor UX/semantics; use sparingly).

## 212. Navigation: Left Nav Flyout (with off-nav closing)
- Slide nav in from left, pushing or overlaying content; close when the user taps outside the nav.

## 213. Navigation: Priority+
- Show as many of the most important items as fit; move the rest into a "More" overflow menu that grows as space shrinks.
- Order items by priority, not alphabetically.

## 214. Navigation: Top Links / Stacked Top Links
- If items are few, keep them as a horizontal row; on narrow screens stack them or wrap into a two-column block.

## 215. Navigation: Sticky Menu / Fixed Nav Overlay / Fixed Middle-Right Nav
- Keep nav reachable during scroll with `position: sticky; top: 0`; keep bar height small on phones so it doesn't steal viewport.

## 216. Navigation: Overlay / Fullscreen Overlay
- Open nav as a layer over content; full-screen variant fills viewport with large tap targets; trap focus and allow Esc to close.

## 217. Navigation: Tabbed Nav / Horizontal Overflow / Flexnav
- Horizontal overflow: let nav scroll sideways (`overflow-x: auto; white-space: nowrap`) and visually hint that more items exist (cut-off item or fade).
- Flexnav: one flexible bar that collapses into a toggle at a breakpoint.

## 218. Navigation: Multi-level (multi-toggle, active-parent links, push menu, mega menu, skip-the-subnav, right-to-left, carousel+)
- Expand nested levels with per-item toggles; keep the parent link clickable separately from its expand control.
- Push menu: slide each submenu level in and provide a "back" to the parent.
- Mega menu: on small screens turn panels into accordions.
- Let users skip subnav (link straight to section page) rather than forcing drill-down.

## 219. Navigation: Breadcrumbs (across top, dropdown, "where am I", last-one-only, to-back, peek)
- Show the full trail on wide screens; on narrow screens show only the last crumb or a "Back to <parent>" link.
- Alternatively collapse middle crumbs into a dropdown/peek control.

## 220. Navigation: Pagination (conditional expose, number→prev/next, stacked)
- On small screens replace numbered links with Prev/Next (plus current page); expose more page numbers as width grows.
- Make targets large enough to tap; stack controls if needed.

## 221. Images: Basic Fluid Image
- `img { max-width: 100%; height: auto; }` so images never overflow their container.

## 222. Images: srcset resolution switching
- Provide multiple widths with `srcset="a-400.jpg 400w, a-800.jpg 800w"` plus `sizes` so the browser downloads the right size/density.

## 223. Images: Picture element & Art direction
- Use `<picture>` with `<source media="...">` to serve different crops or compositions at different sizes (art direction), and `type=` for format fallbacks.
- Always include a fallback `<img>` with `alt`.

## 224. Media: Fluid Video / Fluid iframes / Maps
- Keep embedded video/maps at a fixed aspect ratio while scaling: use `aspect-ratio: 16 / 9; width: 100%` (or the padding-bottom intrinsic ratio hack, see CSS tips).
- Adaptive maps: on small screens show a static map image linking to the full map app; load the interactive map only on larger screens.
- Full-screen iframe: size to viewport only when the embed is the primary content.

## 225. Tables: Responsive table strategies
- Priority columns: tag columns by priority and hide low-priority columns as width shrinks (offer a column toggle).
- Horizontal overflow: wrap the table in a container with `overflow-x: auto`.
- Data-table to list / table to list with header: on small screens display each row as a card, labelling cells via `data-label` and `td::before { content: attr(data-label) }`.
- Header orientation flip: switch headers from top row to left column on narrow screens.
- Link to full table: show a summary/teaser on small screens with a link to the full table.
- Definition list ↔ table and pie chart → table: pick the representation that reads best at each width.
- Comparison table: on small screens compare two items at a time with a selector.

## 226. Charts: Responsive chart
- Resize charts with the container (SVG `viewBox`), simplify labels/ticks at small widths, or swap to a table.

## 227. Forms: Top-to-Left labels
- Put labels above fields on small screens; move labels left of fields when width allows.
- Make inputs `width: 100%` of their container on small screens.

## 228. Forms: Fluid search / search with filters / login
- Search input stretches (flex: 1) with the submit button fixed width beside it.
- Collapse filters behind a toggle on small screens; show inline on wide screens.
- Login form: single column, full-width fields and button on mobile; set input `font-size: 16px` to avoid iOS zoom.

## 229. Text: FitText / responsive lettering
- Scale display headlines to container width (FitText, or CSS `clamp()` / viewport units); never use for body text.

## 230. Text: Responsive footnotes
- Show footnotes in the margin on wide screens; inline/expandable or at the bottom on narrow screens.

## 231. Modules: Carousel (3-up, fluid)
- Show 3 items on wide, fewer on narrow; carousel width is fluid; support swipe on touch.

## 232. Modules: Tabs (transformer, accordion-to-tab, tabs-to-columns, overflow tabs)
- Turn tabs into an accordion on small screens; show as tabs (or side-by-side columns) when wide.
- When tab labels overflow, move extra tabs into a "More" menu.

## 233. Modules: Accordion (to full, to tab, to comparison table, vertical to horizontal)
- Collapse content into accordions on small screens; expand fully, convert to tabs, or into a comparison table when there is space.

## 234. Modules: Messaging (slide-down notification bar, overlay)
- Slide notifications down from the top without covering primary actions; make overlays dismissible.

## 235. Modules: Lightbox (conditional lightbox, accordibox)
- Only open a lightbox when the viewport is large enough; on small screens link directly to the image/content.
- Accordibox: on small screens expand content inline (accordion) instead of a modal.

# Part 13 — CSS craft tips (css-protips)

## 236. CSS reset
- `*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }` for a consistent baseline.

## 237. Inherit box-sizing
- `html { box-sizing: border-box; } *, *::before, *::after { box-sizing: inherit; }` so components/plugins can override it.

## 238. all: unset
- Reset an element's properties in one line: `button { all: unset; }` instead of zeroing each property.

## 239. :not() for nav borders
- `.nav li:not(:last-child) { border-right: 1px solid #666; }` instead of adding then removing borders.

## 240. Locally installed fonts first
- In `@font-face`, list `src: local("Full Name"), local("PostScriptName"), url(...)` so installed fonts skip the download.

## 241. body line-height
- `body { line-height: 1.5; }` (unitless) so all text inherits sane leading.

## 242. :focus styles for form elements
- Style `:focus` on `a, button, input, select, textarea`: e.g. `box-shadow: none; outline: #000 dotted 2px; outline-offset: .05em;`. Never remove focus without replacement.

## 243. Vertically center anything
- Flex: `display:flex; align-items:center; justify-content:center;` on a full-height parent.
- Grid: `display:grid; height:100vh; place-items:center;`.

## 244. aspect-ratio over width/height
- `img { aspect-ratio: 16 / 9; object-fit: cover; }` to keep proportions without hard heights.

## 245. Comma-separated lists
- `ul > li:not(:last-child)::after { content: ","; }`.

## 246. Negative nth-child selection
- Show first N: hide all `li`, then `li:nth-child(-n + 3) { display: block; }`; select the rest with `li:not(:nth-child(-n + 3))`.

## 247. SVG icons
- Use SVG for resolution-independent icons (`background: url(logo.svg)`); for icon-only buttons provide `aria-label` and a fallback that renders `attr(aria-label)`.

## 248. Lobotomized owl
- `* + * { margin-top: 1.5em; }` spaces siblings consistently in flow content.

## 249. Pure-CSS slider with max-height
- Collapse with `max-height` small + `overflow-y: hidden`; on `:hover` raise `max-height` (transitionable) and allow scrolling.

## 250. Equal-width table cells
- `table { table-layout: fixed; }` for equal, predictable column widths (and faster layout).

## 251. Flexbox instead of margin hacks
- Container `display:flex; justify-content: space-between;` with items `flex-basis: 23%` instead of nth-child margin removal.

## 252. Attribute selectors for empty links
- `a[href^="http"]:empty::before { content: attr(href); }` to show the URL when a link has no text.

## 253. :is() for specificity/brevity
- `:is(section, article, aside, nav) :is(h1, h2, h3, h4, h5, h6) { ... }` instead of enumerating combinations.

## 254. Style "default" links
- `a[href]:not([class]) { color: ...; text-decoration: underline; }` to style CMS-inserted unclassed links only.

## 255. Intrinsic ratio boxes
- Container `height: 0; padding-bottom: 20%; position: relative;` (padding % is relative to width → 5:1); child `position:absolute; width:100%; height:100%`. (Prefer `aspect-ratio` today.)

## 256. Style broken images
- `img { display: block; font-family: sans-serif; ... }` then `img::before` (message) / `img::after { content: "(url: " attr(src) ")"; }` — pseudo-elements only render when the image fails.

## 257. rem global, em local
- `html { font-size: 100%; }`; size modules with `rem`; size inner text (h1, p, li) with `em` so components scale from their own root.

## 258. Hide unmuted autoplay video
- User stylesheet: `video[autoplay]:not([muted]) { display: none; }`.

## 259. :root flexible type
- `:root { font-size: calc(1vw + 1vh + .5vmin); }` then `body { font: 1rem/1.6 sans-serif; }` for viewport-scaled typography.

## 260. font-size on form elements
- `input[type="text"], input[type="number"], select, textarea { font-size: 16px; }` to prevent mobile Safari zoom on focus.

## 261. pointer-events for disabled controls
- `button:disabled { opacity: .5; pointer-events: none; }`.

## 262. Hide doubled <br>
- `br + br { display: none; }` to neutralize line breaks used as spacing.

## 263. :empty to hide empty elements
- `:empty { display: none; }` — note whitespace-only elements are not :empty.

## 264. Logical margin shorthands
- `margin-inline: auto;` (left/right) and `margin-block` (top/bottom) — writing-mode aware centering.

# Part 14 — CSS architecture methodologies

## 265. OOCSS (Object-Oriented CSS)
- Separate structure from skin: put layout/box rules and visual themes (colors, gradients, borders) in different reusable classes, combine in markup.
- Separate container from content: don't use location-dependent selectors (`ul li.list-item` → `.list-item`).
- Style elements by their own class so they look the same anywhere in the DOM.

## 266. ACSS (Atomic CSS / utility classes)
- One declaration per class with short names (`.mt-20`, `.fl`, `.di`), composed in HTML.
- Use to avoid one-off rules and CSS bloat; scales well for very large sites.
- Caveat: styling in markup can't change per media query unless you add responsive variants or JS; use utilities as a supplement unless your toolkit supports breakpoint-prefixed utilities.

## 267. BEM (Block, Element, Modifier)
- Name `block`, `block__element`, `block--modifier` (e.g. `.nav`, `.nav__item`, `.nav__item--uplink`).
- Keep names flat — never mirror DOM depth (`block__elem1__elem2` ✗ → `block__elem2` ✓).
- Use it to simulate scoping in global CSS and to make code readable by anyone on the team.

## 268. SMACSS (Scalable & Modular Architecture for CSS)
- Treat as a style guide rather than a framework: categorize rules (base, layout, module, state, theme) and follow its guidelines.
- Combine freely with BEM/OOCSS ideas.

## 269. Choosing a methodology
- No single winner: pick what fits you and your team; author's practice = BEM naming + utility classes where helpful, keeping media queries in CSS.

# Part 15 — GUI architecture patterns (with when-to-use)

## 270. Separated Presentation (core principle)
- Keep domain/model code completely unaware of the UI; presentation depends on domain, never the reverse.
- Put domain logic (e.g. calculations like a variance) in the model, not in event handlers or views.

## 271. Forms and Controls
- Form = app-specific layout + generic widgets; data binding for simple edits, event handlers for form logic.
- Track three state copies: record (DB), session (in-memory), screen (widgets).
- When: small/simple CRUD screens. Avoid for complex screens — the form becomes a god-object hub.

## 272. MVC (classic)
- Model knows nothing of UI; each widget has a View (render) + Controller (handle input → update model); views observe the model.
- Gives multiple synchronized views of one model without them knowing about each other.
- Weakness: Observer flow is implicit/hard to read; view-logic (e.g. "red text when negative") has no clean home.
- When: as principles (separate presentation, sync via events). On mobile, "Apple/Cocoa MVC" collapses V+C → Massive View Controller; OK only for small apps, prototypes, 1–2 screen apps.

## 273. Application Model (VisualWorks)
- Insert an intermediate model holding UI state (selection, enablement) between widgets and domain; bind widgets via property/value objects.
- Avoid letting the application model reach in and manipulate widgets directly — that's the hack that keeps it from being a true Presentation Model.

## 274. Observer Synchronization vs Flow Synchronization
- Observer: widgets update on model events — decoupled, supports multiple views, but hard to trace/debug.
- Flow: code explicitly pushes data to screens at key moments (open, save) — easy to follow, but must know every screen to refresh.
- When: Flow for simple apps / few views; Observer when many views share data.

## 275. MVP (Model-View-Presenter)
- View = dumb widgets that forward gestures to a form-level Presenter; Presenter decides how to update the model (optionally as Command objects → undo/redo).
- View exposes an interface; Presenter depends only on that interface (mock it in tests); keep platform/framework APIs out of the Presenter.
- Risks: lots of manual binding code; presenters accumulate business logic — push domain logic down to model/use-cases.
- When: you need high testability and there's no good binding system.

## 276. MVP — Passive View
- Presenter does every widget update; view has zero logic (fully humble). Best testability; needs a view test double.

## 277. MVP — Supervising Controller
- View handles simple declarative bindings to the model; presenter handles complex logic.
- Smaller presenter, but blurs responsibilities and couples View↔Model; iOS analysis recommends against it.

## 278. Humble View / Humble Object
- Move all behavior out of hard-to-test objects (widgets, Activities, UIViewControllers) into testable classes; leave the view so simple it needs no tests.

## 279. Presentation Model / MVVM
- A UI-framework-independent model of the screen: mirrors domain data plus view state (selected item, isSaveEnabled, formatted strings, colors).
- View binds to it (data binding / observables); ViewModel holds no reference to the view → test without mocking a view.
- Keep computations in the ViewModel, not in binding expressions (XML/template logic is untestable).
- On platforms without native binding, you need reactive/binding libraries — which are easy to misuse and hard to debug.
- When: default for modern UI with binding (Android Architecture Components ViewModel is Google's recommendation; SwiftUI/Vue/Knockout-style apps); good balance of testability and less glue code than MVP.

## 280. Flux / Redux (unidirectional data flow)
- Single source of truth: one store holds state; components render from it and report user actions upward as actions; store notifies subscribers.
- Components never own or mutate the shared source; no duplicate state.
- Use a container/HOC (e.g. `connect` + `Provider` over context) to subscribe and inject state as props; keep views pure.
- Use memoized selectors (reselect) for derived data; never mutate state (return new objects).
- When: many components share and change the same state, or you need predictable, debuggable state transitions (time-travel, logging).

## 281. MVI (Model-View-Intent)
- (Source article failed; derived from the unidirectional-flow sources.) View emits intents → reducer produces a new immutable state → View renders the whole state. Same benefits/when-to-use as Redux, applied per screen on mobile.

## 282. Clean Architecture
- Not a presentation pattern but a layering concept: entities/business objects → use cases → presenters/controllers → UI & data storage at the outer ring; dependencies point inward.
- MVC/MVP/MVVM live in the outer presentation layer.
- When: medium/large apps needing testable, decoupled business logic independent of UI framework and data sources.

## 283. VIPER
- View, Interactor (business logic, data/network), Presenter (UI logic, framework-independent), Entity (plain data), Router (navigation/module assembly).
- Strongest distribution & testability, and explicitly handles navigation (which MV(X) does not).
- Cost: lots of interface/boilerplate for tiny classes. If it feels like building a skyscraper from LEGO, it's too early for VIPER.
- When: large teams/apps with many modules; not for small apps.

## 284. Choosing an architecture
- Judge by distribution (single responsibility), testability, and ease of use (less code = fewer bugs).
- No silver bullet; mixing is fine — start simple (MVC), move complex screens to MVVM/MVP/VIPER individually.
- Simple 1–2 screen app → MVC; testability without binding → MVP; reactive/binding available → MVVM; shared global state → Redux/MVI; large modular apps → Clean/VIPER.

# Part 16 — React component patterns

## 285. Element & Component basics
- A component is a function returning elements; embed values with `{expr}`; pass data in via props; destructure props in the parameter list (`function Greeting({ name })`).

## 286. Default props
- Give optional props fallbacks (`defaultProps` or default parameter values `({ name = "Guest" })`).

## 287. Props in / callbacks out (communication)
- Input via props (declare types with propTypes/TypeScript); output via callback props; never read a child's state directly.

## 288. JSX spread attributes
- Split own props from platform props with rest: `({ title, ...rest }) => <div {...rest}>`; don't spread unknown props onto DOM elements blindly (react-bits anti-pattern).

## 289. Merge className / props
- `["btn", className].filter(Boolean).join(" ")` (or clsx/classnames); mind spread order so consumer values win or lose intentionally.

## 290. Conditional rendering
- Use `cond && <X/>`, `a || b`, ternaries; for many cases use a component switch (object map from value → component).

## 291. Children types / array as children
- Render lists with `items.map(i => <li key={i.id}>…</li>)`; use stable ids as keys, never array indexes for reorderable lists.
- Treat `children` as opaque; use `React.Children.only` when exactly one child is required.

## 292. Render props / function as children
- Component calls `children(value)` or `render(value)`; consumer decides the markup (`<Width>{w => …}</Width>`). Use to share behavior while delegating rendering.

## 293. Composition (children API, elements as props)
- Compose via `children` so parents don't hard-code dependencies; pass named elements as props (`title={<Title/>}`) for multiple slots.

## 294. Proxy component
- Wrap a lower-level element to preset props everywhere (`<Button>` always `type="button"`).

## 295. Style component
- Layer style-only proxies (`PrimaryBtn → Btn → button`) to centralize class-name logic.

## 296. Layout component
- Static structural wrappers (split panes, stacks); can skip re-render since children update themselves — but avoid premature optimization.

## 297. Event switch
- One handler switching on `event.type` when handling many events; inline arrows for trivial cases.

## 298. Container vs Presentational
- Container fetches/subscribes to data and renders a presentational component; presentational components are stateless and style-only. Write different containers for different contexts.

## 299. Higher-order component (HOC)
- `withX(Component)` returns an enhanced component (data, tracking, feature flags, styling, props proxy). Use to hide setup/config and inject only needed props; makes the wrapped component easy to test.

## 300. Dependency injection
- Don't import/construct dependencies inside components; provide via context and inject with a `wire(Component, deps, mapper)`-style HOC (Redux `connect`/`Provider` do this).

## 301. Context wrapper / Provider
- Share cross-cutting values (theme, store, i18n) via context instead of prop drilling.

## 302. State hoisting
- Lift shared state to the nearest common parent; children call callbacks. Keep leaf components stateless.

## 303. Controlled input
- `value` from state + `onChange` updating state; the UI always reflects app state.

## 304. setState correctness
- setState is async: pass an updater function when new state depends on previous state; never mutate state; don't copy props into initial state (it goes stale).

## 305. Fragments
- Group children without extra DOM nodes (`<>…</>`).

## 306. Feature flags / UX variations
- Gate features with a flag HOC/component; compose variations (toggle elements, display-order variations) rather than forking components.

## 307. Performance
- Avoid wasted renders with shouldComponentUpdate / PureComponent / memo; memoize derived data with selectors; beware new object/function props breaking pure checks.

## 308. Styling components
- Prefer stateless UI components, CSS modules for scoping, style functions computed from props, base/layout/typography components for consistency.

## 309. Avoid legacy anti-patterns
- No findDOMNode, mixins, setState in componentWillMount; use synthetic events knowing their pooling/wrapping behavior.

# Part 17 — Vue patterns

## 310. Component declaration
- Default to Single-File Components (`<template>`, `<script>`, `<style scoped>`); alternatives: render functions (`h()`), JSX, class components.

## 311. Props down, events up
- Children treat props as read-only; notify parents with `$emit('event', payload)`; parent listens `@event` and updates its own data.

## 312. Conditional rendering
- `v-if/v-else-if/v-else` add/remove DOM; `v-show` toggles CSS display — prefer `v-show` for frequent toggles.
- Group multiple elements with `<template v-if>` (no wrapper node); in render functions use a component map lookup.

## 313. Dynamic component
- `<component :is="current">`; wrap in `<keep-alive>` to preserve state when switching (tabs).

## 314. Functional component
- Stateless, instance-less (`<template functional>`, read `props.x`) for cheap presentational pieces.

## 315. Renderless component
- Encapsulate logic, render nothing itself: `render() { return this.$scopedSlots.default(data) }`; consumer supplies markup via scoped slot.

## 316. Composition
- Prefer nesting components; use `extends` for one base; mixins for shared options (use sparingly); use `v-slot` (2.6+) not `slot`/`slot-scope`.

## 317. Passing props & listeners (wrappers)
- Forward with `v-bind="$attrs" v-on="$listeners"` and set `inheritAttrs: false` to avoid double-binding on the root.

## 318. Higher-order component
- Function taking a component and returning an enhanced one; in Vue prefer slots/renderless components where possible.

## 319. Provider / Consumer
- Provider holds state + actions and exposes via scoped slot (`v-slot="{ state, actions }"`); consumer is a functional presentational component.

## 320. Dependency injection (provide/inject)
- `provide` on ancestor, `inject` in descendants to avoid prop drilling; injections aren't reactive unless you provide an observed object; give `inject` a `default`.

## 321. Error handling
- Error-boundary wrapper using `errorCaptured(err, vm, info)`; render fallback UI; return `false` to stop propagation.

## 322. Productivity: immediate watchers
- `watch: { q: { handler: 'fetch', immediate: true } }` instead of duplicating the call in `created`.

# Part 18 — Mobile architecture patterns (iOS & Android)

## 323. Evaluation criteria
- Distribution (strict single responsibilities), testability (follows from distribution), ease of use (code volume = maintenance cost).

## 324. Apple (Cocoa) MVC on iOS
- Controller mediates View↔Model; in practice UIViewController owns lifecycle, delegates, data sources, networking → Massive View Controller, hard to test.
- When: small pet projects or fast prototypes only.

## 325. MVC on Android
- Model = data/state/business logic (UI-independent, reusable); View = XML/Compose; Controller = Activity/Fragment.
- Keep layout/resources in XML; move drawing code out of Activities/Fragments.
- Concern: controller tied to Android APIs (hard to unit test) and bloats. Fine for 1–2 screen apps.

## 326. MVP on mobile (Passive View)
- Activity/Fragment/UIViewController implements a View interface; Presenter has no framework/UIKit imports and holds view state; inject a mock view in tests.
- Needs a separate assembly place (Router/DI). Lots of manual binding code; watch for presenters bloating with business logic.

## 327. MVVM on mobile
- ViewModel wraps model, exposes observable state + actions, holds no view reference; View binds (Android Data Binding/LiveData, iOS KVO/RxSwift/Combine).
- Keep logic out of XML binding expressions; reactive code can be hard to debug.
- Google-recommended on Android via Architecture Components ViewModel; MVP vs MVVM largely preference, MVVM = less code with binding.

## 328. VIPER on iOS
- Module = View + Interactor + Presenter + Entity + Router; best separation and navigation handling; heavy boilerplate — reserve for large apps.

## 329. Clean Architecture on Android
- Layers: entities → use cases → presenters → UI/data; MVC/MVVM sit in the presentation ring; aim for testable, extensible, decoupled code.

## 330. Mixing architectures
- Start with the simplest that works; migrate only complex screens to heavier patterns; patterns coexist in one app.

## 331. Builder (Android)
- Use step-by-step builders for objects with many optional settings (`AlertDialog.Builder().setTitle().setMessage().setPositiveButton().show()`).

## 332. Dependency Injection (Android)
- Supply network clients, image loaders, SharedPreferences from outside (Dagger `@Module/@Provides/@Component/@Inject`, Hilt, Koin) so Activities/Fragments don't build dependencies.

## 333. Singleton
- Kotlin `object` for truly single resources (DB/network connection); avoid overuse — global mutable state causes hidden side effects.

## 334. Factory
- Centralize creation of interface-sharing types; beware a bloated, hard-to-test factory.

## 335. Adapter
- Bridge domain data to framework widgets: `RecyclerView.Adapter` inflates rows, binds items to `ViewHolder`s, reports item count — the list never knows your model.

## 336. Facade
- Hide multi-layer data access (cache, DB, API) behind one interface (Retrofit API interface + OkHttp interceptors/converters) so UI code stays concise.

## 337. Decorator
- Stack optional behaviors around a base object at runtime; wrapping order matters.

## 338. Composite
- Treat leaves and groups uniformly via a shared interface for hierarchical UI/data (nested groups, view trees).

## 339. Command / Event bus
- Wrap requests as objects to decouple sender/receiver (e.g. EventBus: register in `onStart`, unregister in `onStop`, `@Subscribe(threadMode = MAIN)`); compensate harder-to-trace flow with tests.

## 340. Observer
- One-to-many change notification for async data/user input: LiveData/Flow or Rx with `subscribeOn(Schedulers.io())` and `observeOn(AndroidSchedulers.mainThread())` so UI updates happen on the main thread.

## 341. Strategy
- Swap interchangeable behaviors at runtime behind one interface without changing the client.

## 342. State
- Put each state's behavior in its own class (e.g. Ready / NoInk) instead of growing conditionals; switch the state object on transitions.

# Part 19 — Design principles

## 343. Single Responsibility Principle (SRP)
- Intent: A module/class should have one reason to change.
- Use when: Always, as a review heuristic; a class that changes for both UI and persistence reasons should split.
- Structure/how: Group code by the actor/concern that drives change; extract classes when a second concern appears.
- Pros: smaller, testable units; localized change. Cons/pitfalls: over-splitting into anemic micro-classes; "responsibility" is judgment-dependent.
- Related to / UI example: Separate a component's rendering from its data fetching (container/presentational split). State and Decorator patterns are cited by refactoring.guru as SRP-supporting.

## 344. Open/Closed Principle (OCP)
- Intent: Extend behavior without editing existing, working source.
- Use when: A variation point is known to recur (new payment types, new shapes, new subscribers).
- Structure/how: Depend on abstractions; add new implementations (Strategy, Observer subscribers, Composite node types, State classes).
- Pros: lowers regression risk. Cons/pitfalls: speculative abstraction everywhere violates YAGNI; open only where change is real.
- Related to / UI example: Adding a new widget type to a component tree without touching the renderer.

## 345. Liskov Substitution Principle (LSP)
- Intent: A subtype must be usable wherever its parent is expected without breaking callers.
- Use when: Designing any inheritance or interface implementation.
- Structure/how: Subtypes keep the parent's contracts (preconditions no stronger, postconditions no weaker, invariants preserved).
- Pitfalls: circle-ellipse / square-rectangle problem (subtyping by value, not behavior); "Refused Bequest" smell; throwing UnsupportedOperation in overrides.
- Related to: Prefer composition or distinct types when substitution fails.

## 346. Interface Segregation Principle (ISP)
- Intent: Many small, client-specific interfaces beat one fat interface.
- Use when: Implementers are forced to stub methods they do not need.
- Structure/how: Split by client role; compose interfaces.
- Pitfalls: Interface bloat anti-pattern is the failure mode; too many tiny interfaces fragment the model.
- Related to / UI example: Component props typed per role (e.g., `Clickable`, `Focusable`) instead of one giant props bag.

## 347. Dependency Inversion Principle (DIP)
- Intent: High-level policy and low-level detail both depend on abstractions; details depend on policy, not vice versa.
- Use when: Business logic would otherwise import concrete DB/HTTP/UI code.
- Structure/how: Define interfaces owned by the high-level module; inject implementations (Dependency Injection, Service Locator, Hexagonal/Clean architecture ports).
- Pros: testable, swappable. Cons: indirection; hidden wiring if overdone.
- Related to: Fixes Circular dependency anti-pattern.

## 348. Composition Over Inheritance
- Intent: Build behavior by combining small objects rather than deep subclass trees (GoF principle; Effective Java item 16).
- Use when: A class varies along two or more independent axes (e.g., log destination x filter) - inheritance yields m x n subclasses ("subclass explosion").
- Structure/how: Adapter (wrap a destination to look like what the client accepts), Bridge (split abstraction from implementation and combine at runtime), Decorator (same interface, stackable wrappers), or simply hold lists of collaborators (logger with lists of filters and handlers).
- Pitfalls to avoid (python-patterns.guide): one class with many `if` flags scatters features and runs every check every time; multiple inheritance breaks on init conflicts, name collisions and MRO, and per-base unit tests can pass while the combo fails; mixins reduce but do not remove those liabilities; generating classes with `type()` hurts readability, debugging and tooling.
- Effective Java angle: inheritance breaks encapsulation (subclass depends on superclass implementation); use forwarding/wrapper classes; design and document for inheritance or forbid it.
- Related to / UI example: React-style composition (children/slots, hooks) instead of component class hierarchies; game Component pattern.

## 349. Encapsulate What Varies
- Intent: Isolate the parts most likely to change behind a stable interface.
- Use when: Identifying a variation point.
- Structure/how: Extract the varying algorithm/representation into its own object (Strategy, State, Bridge).
- Pitfalls: guessing the wrong axis of change.
- Related to: OCP, Strategy.

## 350. Program to an Interface, Not an Implementation
- Intent: Callers depend on types/contracts, not concrete classes (Effective Java item 52: declare variables using interface types).
- Use when: Any collaborator that could vary or be mocked.
- Structure/how: Declare fields/params as interfaces; create concretes in factories or composition root.
- Pitfalls: interface-per-class ceremony with only one implementation forever.

## 351. DRY (Don't Repeat Yourself)
- Intent: Each piece of knowledge has a single authoritative representation.
- Use when: Same rule appears in several places.
- Structure/how: Extract functions/modules/constants; generate derived artifacts.
- Pitfalls: merging code that is only coincidentally similar couples unrelated concepts (wrong abstraction).
- Related to: Copy-and-paste programming, Shotgun surgery anti-patterns.

## 352. KISS / Do the Simplest Thing That Could Possibly Work
- Intent: Simpler systems have fewer bugs and are easier to change.
- Use when: Choosing between designs.
- Pitfalls: "simple" must still solve the real problem; simplicity is not the same as easy/hacky.
- Related to: Design-patterns-for-humans takeaway - apply a pattern only when its problem actually exists.

## 353. YAGNI
- Intent: Build features only when needed, not when anticipated.
- Pitfalls: ignoring known near-term requirements; Overengineering and Speculative Generality are the opposite failures.

## 354. Separation of Concerns
- Intent: Divide a program into parts each handling one concern (business logic vs UI vs persistence).
- Structure/how: Layers, modules, MV* patterns.
- Related to / UI example: Model/View separation; CSS vs markup vs behavior.

## 355. Minimize Coupling / Maximize Cohesion
- Intent: Modules depend on each other as little as possible; each module groups closely related responsibilities.
- Structure/how: Narrow interfaces, events/mediators instead of direct references, group by feature.
- Pitfalls: decoupling via global event buses hides dependencies (see Event Queue caveats).

## 356. Law of Demeter
- Intent: An object talks only to itself, its params, objects it creates and its direct fields ("don't talk to strangers").
- Pitfalls: Message Chains smell (`a.b().c().d()`) is the violation; blind application adds Middle Man wrappers.

## 357. Orthogonality
- Intent: Unrelated concepts are independent; changing one does not affect others.
- Related to: SRP, Separation of Concerns.

## 358. Inversion of Control
- Intent: The framework calls your code rather than you calling everything ("Hollywood principle").
- Related to: Game Loop (engine vs library distinction), Template Method, Dependency Injection, UI event handlers.

## 359. Hide Implementation Details / Minimize Accessibility
- Intent: Expose the minimal public surface so internals can change (Effective Java 13-14: minimize accessibility, use accessors not public fields).
- Pitfalls: Object orgy anti-pattern is the failure mode.

## 360. Command-Query Separation (CQS)
- Intent: A method either changes state or returns data, never both.
- Related to: CQRS at architecture scale; predictable UI selectors vs actions.

## 361. Robustness Principle
- Intent: Be strict in what you send, tolerant in what you accept when meaning is clear.
- Pitfalls: excessive tolerance can entrench malformed input; pair with validation at boundaries.
- Related to: Tolerant Reader pattern.

## 362. Code for the Maintainer / Boy-Scout Rule / Curly's Law
- Intent: Write for future readers; leave code cleaner than found; each unit does one thing well.

## 363. Avoid Premature Optimization
- Intent: Write clear code first; profile; optimize measured bottlenecks (Effective Java 55).
- Related to: Game patterns (Data Locality, Object Pool, Dirty Flag) are explicitly optimizations to use only when measurement justifies them.

## 364. Prefer Immutability
- Intent: Make classes immutable unless there is a strong reason not to (Effective Java 15); immutable objects are thread-safe and freely shareable.
- Structure/how: Final fields, no setters, defensive copies (item 39), return new instances.
- Pros: simpler reasoning, safe caching/sharing (Flyweight). Cons: allocation per change; use builders/companion mutable types for heavy construction.
- Related to / UI example: Immutable state trees enable cheap change detection (reference equality) in React/Redux.

## 365. Effective Java: Object creation rules
- Intent: Make construction clear and safe.
- Use when: Designing APIs.
- Structure/how: Static factory methods instead of constructors (named, can cache, can return subtypes) [1]; Builder for many params [2]; enforce singletons via single-element enum [3]; private constructor for utility classes [4]; avoid needless objects/autoboxing [5]; null out obsolete references in self-managed memory [6]; avoid finalizers [7].
- Pitfalls: static factories are harder to discover and prevent subclassing.

## 366. Effective Java: Object contracts
- equals must be reflexive, symmetric, transitive, consistent, non-null [8]; always override hashCode with equals [9]; override toString [10]; prefer copy constructors/factories to clone [11]; implement Comparable for natural orders [12].

## 367. Effective Java: Class and interface design
- Prefer interfaces to abstract classes, ship skeletal implementations [18]; interfaces define types, not constant holders [19]; prefer class hierarchies to tagged classes [20]; represent strategies as function objects [21]; prefer static nested classes [22]; use marker interfaces to define types [37].

## 368. Effective Java: Generics and enums
- No raw types [23]; eliminate unchecked warnings narrowly [24]; lists over arrays [25]; favor generic types and methods [26-27]; PECS bounded wildcards (producer-extends, consumer-super) [28]; typesafe heterogeneous containers [29]; enums instead of int constants [30]; instance fields not ordinals [31]; EnumSet over bit fields [32]; EnumMap over ordinal arrays [33]; extensible enums via interfaces [34]; annotations over naming patterns [35]; always @Override [36].

## 369. Effective Java: Method design
- Validate parameters early [38]; defensive copies [39]; careful signatures - short param lists, enums over booleans [40]; overload sparingly [41]; varargs judiciously [42]; return empty collections, not null [43]; document every exposed element [44].

## 370. Effective Java: General programming
- Minimize local variable scope [45]; prefer for-each [46]; know the libraries [47]; no float/double for money [48]; primitives over boxed [49]; avoid strings where better types exist [50]; StringBuilder for concatenation [51]; interfaces over reflection [53]; native methods sparingly [54]; follow naming conventions [56].

## 371. Effective Java: Exceptions
- Exceptions only for exceptional conditions, never control flow [57]; checked for recoverable, runtime for programming errors [58]; use checked exceptions sparingly and offer state-test methods [59]; reuse standard exceptions [60]; translate exceptions to the layer's abstraction with cause chaining [61]; document every thrown exception [62].
- Related to: Error hiding anti-pattern.

# Part 20 — Creational patterns

## 372. Simple Factory
- Intent: A helper creates objects so callers skip construction details.
- Use when: Creation involves logic that should not be repeated at call sites.
- Structure/how: A function/static method returns a configured instance.
- Pros: centralizes creation. Cons: not a GoF pattern; one switch-based factory grows with every new type.
- Related to / UI example: `createButton(variant)` returning configured component.

## 373. Factory Method
- Intent: A base class defines a creation hook; subclasses (or a class/instance attribute holding a callable, in Python) decide the concrete type.
- Use when: The workflow is generic but the product class is decided at runtime or by subclass.
- Structure/how: Creator declares `createProduct()`; concrete creators override; client uses Product interface. Python: accept any callable as the factory; dependency injection is a lighter alternative.
- Pros: decouples creator from concrete products; OCP. Cons: parallel creator/product hierarchies.
- Related to / UI example: Cross-platform dialog creating Windows vs web buttons; often evolves into Abstract Factory.

## 374. Abstract Factory
- Intent: Produce families of related objects that must match, without naming concrete classes.
- Use when: Products must be compatible (wooden door + carpenter; dark-theme widgets together).
- Structure/how: Factory interface with one create method per product; one concrete factory per family. Python: pass callables/classes instead of factory class hierarchies.
- Pros: guarantees consistent families. Cons: adding a new product type changes every factory.
- Related to / UI example: Theme/skin factories producing matching Button, Checkbox, Menu.

## 375. Builder
- Intent: Construct a complex object step by step.
- Use when: Many optional parameters (telescoping constructors) or multi-step creation; Effective Java 2.
- Structure/how: Builder accumulates settings via fluent setters, `build()` validates and returns (often immutable) product; optional Director encodes recipes.
- Pros: readable construction, immutability, validation in one place. Cons: extra class; in Python, keyword arguments often make it unnecessary (python-patterns.guide notes builders mostly simulate optional args).
- Related to / UI example: Query builders, request builders, form/schema builders. Step Builder variant enforces order via types.

## 376. Prototype
- Intent: Create objects by copying an existing instance.
- Use when: Copying is cheaper than building, or the concrete class is unknown to the caller.
- Structure/how: `clone()` on a prototype interface; prototype registry of preconfigured instances.
- Pitfalls: deep vs shallow copy; circular references; Java's `clone` is broken - prefer copy constructors (Effective Java 11).
- Related to: JS prototypal inheritance (`Object.create`); game Prototype (spawner clones a template monster; data-driven prototypes in JSON).

## 377. Singleton
- Intent: One instance with global access.
- Use when: Truly single resource (but see alternatives).
- Structure/how: Private constructor + static accessor with lazy creation; Java: single-element enum; Python: module-level Global Object instead.
- Pros: guaranteed single instance; lazy init.
- Cons/pitfalls: violates SRP (controls instances and gives access); global state and hidden coupling; thread-safety of lazy init; hard to mock/test; many treat it as an anti-pattern. Game Programming Patterns: prefer passing objects, using a base class accessor, or Service Locator.
- Related to: Global Object (Python), Monostate, Multiton, Service Locator, Dependency Injection.

# Part 21 — Structural patterns

## 378. Adapter
- Intent: Make an incompatible interface work with code expecting another.
- Use when: Reusing a class (library, legacy) without modifying it.
- Structure/how: Adapter implements target interface and delegates to adaptee (object adapter) or inherits it (class adapter).
- Pros: SRP, OCP. Cons: extra layer; many adapters signal a missing abstraction.
- Related to / UI example: Wrapping a third-party chart lib behind your own component API; Anti-Corruption Layer at system scale.

## 379. Bridge
- Intent: Separate abstraction from implementation so both vary independently.
- Use when: Inheritance would multiply (every page x every theme; every shape x every renderer).
- Structure/how: Abstraction holds a reference to an Implementor interface; both hierarchies extend independently.
- Pros: avoids subclass explosion; swap implementation at runtime. Cons: harder up-front design.
- Related to / UI example: Pages with swappable themes; remote controls x devices.

## 380. Composite
- Intent: Treat single objects and groups uniformly in a tree.
- Use when: Part-whole hierarchies where clients should not distinguish leaf from container.
- Structure/how: Component interface; Leaf does work; Container holds children (via Component interface), delegates down and aggregates results; client uses Component only.
- Pros: recursion/polymorphism simplify trees; OCP for new node types. Cons: overly general interface when node types differ greatly (e.g., `add()` on leaves).
- Related to / UI example: UI component/DOM trees, Tkinter widget trees, file systems, org charts. Pairs with Builder (build trees), Chain of Responsibility (bubble to root - DOM event bubbling), Iterator/Visitor (traverse), Flyweight (share leaves).

## 381. Decorator (Wrapper)
- Intent: Add behavior at runtime by wrapping an object with the same interface.
- Use when: Need combinable add-ons without a subclass per combination; class is final.
- Structure/how: Base decorator holds wrapped component and forwards; concrete decorators add before/after behavior; client stacks them.
- Pros: runtime composition; SRP. Cons: hard to remove a specific wrapper from the stack; order-dependent behavior; messy setup code; identity checks break.
- Related to / UI example: Higher-order components, middleware, stream wrappers, logging/caching wrappers. "Decorator changes the skin, Strategy changes the guts." Python `@decorator` is a function-wrapping cousin.

## 382. Facade
- Intent: A simple interface over a complex subsystem.
- Use when: Clients need only common operations.
- Structure/how: Facade class orchestrates subsystem objects; subsystem remains accessible for advanced use.
- Pitfalls: facade becoming a God object; hiding needed flexibility.
- Related to / UI example: jQuery `$()` over DOM APIs; an `api.ts` module over fetch/auth/retry; computer power button.

## 383. Flyweight
- Intent: Share common (intrinsic) state among many objects to save memory; extrinsic state is passed in.
- Use when: Huge numbers of similar objects and memory is a concern.
- Structure/how: Flyweight factory caches shared immutable instances; contexts store unique state. Python: decide factory vs constructor caching.
- Pros: big RAM savings. Cons: CPU cost of passing/recomputing extrinsic state; complexity; shared state must be immutable.
- Related to / UI example: Glyph objects in text editors; JS event delegation (one handler for many items, per Osmani); game terrain/tree instancing.

## 384. Proxy
- Intent: A stand-in that controls access to a real object.
- Use when: Lazy loading (virtual proxy), access control (protection proxy), remote access, caching, logging.
- Structure/how: Same interface as the service; proxy manages service lifecycle.
- Pros: transparent to client. Cons: added latency/indirection.
- Related to / UI example: JS `Proxy` for reactive state (Vue), lazy image placeholders, API caching layers. Differs from Decorator: proxy controls lifecycle, decorator composition is client-controlled.

# Part 22 — Behavioral patterns

## 385. Chain of Responsibility
- Intent: Pass a request along handlers until one handles it.
- Use when: Several objects may handle a request and the handler is known only at runtime.
- Structure/how: Handlers share an interface and link to the next; each handles or forwards; can stop propagation.
- Pros: decouples sender from receivers; order configurable. Cons: request may go unhandled; debugging flow.
- Related to / UI example: DOM event bubbling, middleware pipelines (Express), help/tooltip lookup up a widget tree. Unlike Decorator, a handler can stop the flow.

## 386. Command
- Intent: Wrap a request as a standalone object with all info to execute it.
- Use when: Parameterize objects with operations; queue/schedule/log/remote-execute; undo/redo; transactions.
- Structure/how: Command interface `execute()` (and `undo()`); concrete commands hold receiver + args; invoker (button, menu, shortcut) holds a command; client wires receiver -> command -> sender.
- Pros: decouples invoker and receiver; OCP; undo/redo; macro (composite) commands. Cons: extra layer and class count; undo needs state backups (memory) or inverse operations (sometimes impossible).
- Related to / UI example: Toolbar button, menu item, and keyboard shortcut sharing one Copy command; undo stack in editors; Redux actions. Pair with Memento for undo; Prototype to copy into history. Game: input handling remaps buttons to commands; replay; AI driving actors via same commands.

## 387. Iterator
- Intent: Traverse a collection without exposing its structure.
- Use when: Uniform traversal over varied/complex structures.
- Structure/how: Iterator with next/hasNext (or language protocol: Python `__iter__`/`__next__`, JS `Symbol.iterator`); keep iterable and iterator separate so multiple traversals can coexist.
- Pitfalls: concurrent modification; objects that are their own iterator can be consumed only once.
- Related to: Generators; Composite traversal.

## 388. Mediator
- Intent: Central object coordinates peers so they do not reference each other.
- Use when: Many-to-many interactions are tangled (chat room, form fields that affect each other).
- Structure/how: Components notify mediator; mediator decides who reacts.
- Pros: reduces coupling; reuse components. Cons: mediator can become a God object.
- Related to / UI example: Dialog controller coordinating inputs; air traffic control; often implemented on Observer. React: lifting state up into a parent acts as mediator.

## 389. Memento
- Intent: Capture and restore an object's state without exposing internals.
- Use when: Undo, snapshots, checkpoints.
- Structure/how: Originator creates opaque memento; caretaker stores history.
- Pitfalls: memory cost of many snapshots; caretakers must track originator lifecycle.
- Related to / UI example: Undo history with Command; editor state snapshots; immutable state history (time-travel debugging).

## 390. Observer
- Intent: Subscription mechanism - dependents are notified when a subject changes.
- Use when: A change must trigger updates in an unknown or changing set of objects; objects watch others temporarily.
- Structure/how: Publisher keeps a subscriber list with subscribe/unsubscribe; subscribers share a notify interface; publisher loops and notifies with event data.
- Pros: OCP (new subscribers without changing publisher); runtime relationships. Cons/pitfalls: notification order not guaranteed; memory leaks from forgotten unsubscriptions (lapsed listener); cascading updates; synchronous notification can hurt performance (game: observers run inline - keep them fast or use Event Queue).
- Related to / UI example: UI event listeners (button clicks), data binding, reactive stores, RxJS. Mediator often built on Observer.

## 391. State
- Intent: Object changes behavior when internal state changes, as if changing class.
- Use when: Behavior depends on state, many states, frequent change, large conditionals on state fields.
- Structure/how: Context holds current State object and delegates; State interface declares state-dependent methods; concrete states may trigger transitions on the context.
- Pros: SRP, OCP, removes conditionals. Cons: overkill for few/rarely changing states.
- Related to / UI example: UI state machines (idle/loading/success/error), media player, network connection, character controller (game: FSM, hierarchical and pushdown automata). State is like Strategy, but states know each other and drive transitions.

## 392. Strategy
- Intent: Interchangeable algorithms behind one interface, chosen at runtime.
- Use when: Several ways to do a task; replace conditionals selecting algorithm variants.
- Structure/how: Context holds a strategy reference; client injects. In modern languages, a function/lambda is enough (Effective Java 21).
- Pros: OCP; isolates algorithm. Cons: clients must know differences; overkill if algorithms rarely change.
- Related to / UI example: Sort/compare functions, validation rules, layout algorithms, pricing rules.

## 393. Template Method
- Intent: Base class fixes algorithm skeleton; subclasses override steps.
- Use when: Variants share flow but differ in steps.
- Structure/how: Final template method calls abstract/hook steps.
- Pros: reuse of invariant flow. Cons: inheritance coupling; LSP risk; harder to follow as steps grow.
- Related to: Fixes "Call super" anti-pattern; Strategy is the composition-based alternative. UI example: framework lifecycle hooks (componentDidMount).

## 394. Visitor
- Intent: Add operations to a stable object structure without changing its classes.
- Use when: Structure is stable but new operations are frequent (AST passes, exporters).
- Structure/how: Elements `accept(visitor)` and call `visitor.visitX(this)` (double dispatch).
- Pros: OCP for operations; groups related behavior. Cons: adding element types requires changing every visitor; may need access to private fields.
- Related to: Composite traversal; Acyclic Visitor; pattern matching replaces it in many modern languages.

## 395. Interpreter
- Intent: Represent a grammar as classes and evaluate sentences.
- Use when: Simple DSLs or rule languages.
- Pitfalls: poor performance/maintenance for complex grammars; use parser generators.
- Related to: Game Bytecode pattern is the faster, flattened alternative.

# Part 23 — JavaScript-specific patterns (Addy Osmani, Learning JS Design Patterns)

## 396. Module Pattern
- Intent: Encapsulate private state and expose a public API, emulating classes/namespaces.
- Use when: Pre-ES-modules code, or any unit needing private state.
- Structure/how: IIFE returns an object literal; closure keeps private variables. Modern: ES modules with import/export (book ch. 5).
- Pros: privacy, avoids global pollution. Cons: private members hard to test/extend; changing visibility means editing every reference. [general knowledge]
- Related to: Global Object (Python module-level objects).

## 397. Revealing Module Pattern
- Intent: Define all functions privately, then return an object mapping public names to chosen private functions.
- Structure/how: `return { publicName: privateFn }` at the end.
- Pros: consistent syntax; readable public API at a glance. Cons: patching a public function does not change private internal references, so overrides are fragile. [general knowledge]

## 398. JS Singleton
- Intent: Single shared instance via module scope or lazy getInstance closure.
- Pitfalls: ES modules are already singletons; overuse indicates poor module design and complicates testing (Osmani warns similarly). [general knowledge]

## 399. Observer / Publish-Subscribe
- Intent: Observer: subject keeps observer list. Pub/Sub: an event channel sits between publishers and subscribers so neither knows the other.
- Structure/how: `subscribe(topic, fn)`, `publish(topic, data)`, `unsubscribe(token)`.
- Pros: loose coupling; great for event-driven UIs. Cons: hard to guarantee parts work as expected (publisher assumes someone listens); subscribers unaware of each other; dynamic links hard to trace/debug. [general knowledge]
- Related to / UI example: DOM `addEventListener`, Node `EventEmitter`, Gmail/stock-ticker examples in the book, RxJS observables, Redux store subscription.

## 400. Mediator (JS)
- Intent: Centralize communication between modules/components.
- Pros: reduces many-to-many channels. Cons: single point of failure and potential bottleneck. [general knowledge]
- Related to / UI example: Book ch. 12 shows a React mediator; form controller or app-level event coordinator.

## 401. Prototype (JS)
- Intent: Objects inherit directly from other objects (`Object.create`), sharing methods via the prototype chain.
- Pros: memory efficient method sharing; native to the language. Cons: shared mutable properties on prototypes leak between instances.

## 402. Command (JS)
- Intent: Decouple invoking an action from its implementation via an `execute(name, ...args)` dispatcher.
- Related to / UI example: Undoable actions, keyboard shortcut maps, Redux action objects.

## 403. Facade (JS)
- Intent: Simple API over complex/cross-browser behavior.
- Pitfalls: hidden performance cost of the abstraction. [general knowledge]
- Related to / UI example: jQuery's `$(el).css()`/`.ready()` hide browser differences.

## 404. Factory (JS)
- Intent: A function that returns objects based on input, without `new` or class knowledge at the call site.
- Use when: Object setup is complex or depends on environment; many small objects share properties.
- Pitfalls: unnecessary indirection for simple objects; harder testing if overused. [general knowledge]
- Related to / UI example: `createElement(type, props)`, vehicle/truck factory examples in the book.

## 405. Mixin
- Intent: Reuse behavior by copying/composing methods into objects or classes (subclass factories `Base => class extends Base`).
- Pros: lightweight reuse without deep hierarchies. Cons: prototype pollution, name collisions, unclear provenance of methods. [general knowledge]
- Related to: python-patterns.guide warns mixins keep most multiple-inheritance liabilities; prefer composition/hooks.

## 406. Decorator (JS)
- Intent: Augment objects dynamically by wrapping or extending them; TC39 decorators for classes.
- Pitfalls: many small wrapper objects complicate debugging. [general knowledge]
- Related to / UI example: Higher-order components, function wrappers (debounce/memoize).

## 407. Flyweight (JS)
- Intent: Share intrinsic data across many objects; event-handling variant uses one delegated handler on a parent instead of many listeners.
- Related to / UI example: Event delegation on lists/tables; book catalog example separating intrinsic book data from extrinsic checkout state.

## 408. MVC
- Intent: Separate Model (data/domain), View (presentation), Controller (input handling/coordination).
- Pros: separation of concerns; parallel work; testable models. Cons: controller bloat; tight View-Controller coupling in practice.
- Related to / UI example: Classic Backbone-era apps; Observer links model to views.

## 409. MVP
- Intent: Presenter holds presentation logic; passive View exposes an interface the presenter drives.
- Pros: views are thin and mockable; presenter fully testable. Cons: presenter grows large; verbose view interfaces.

## 410. MVVM
- Intent: ViewModel exposes observable state and commands; the View binds declaratively.
- Pros: data binding removes glue code; testable ViewModel. Cons: binding magic hard to debug; memory cost of bindings; overkill for simple UIs.
- Related to / UI example: Knockout, Vue, Angular; MVI/Flux/unidirectional data flow as successors.

# Part 24 — Game programming patterns (Robert Nystrom)

## 411. Game Loop
- Intent: Decouple progression of game time from user input and processor speed.
- Use when: Nearly every game/real-time sim; engines own it (engine calls you vs library you call).
- Structure/how: Loop: process input (non-blocking) -> update -> render. Options: unbounded (speed tied to hardware - bad); frame-limited sleep; variable timestep (adapts, but nondeterministic and physics-unstable); fixed timestep with catch-up accumulator (stable, deterministic; render may be skipped); render interpolation using leftover fraction for smooth motion.
- Pitfalls: update step must exceed update cost on slowest hardware or the game spirals - cap catch-up iterations; platform event loops (browser `requestAnimationFrame`) may own the loop; battery/heat - clamp FPS on mobile.
- Related to / UI example: Animation frame loops in web apps; Update Method; Double Buffer.

## 412. Update Method
- Intent: Simulate many independent objects by each advancing one frame per call.
- Use when: Many live entities with mostly independent time-based behavior.
- Structure/how: World holds collection; each entity has `update(dt?)`; loop calls each per frame; each stores its own state between frames.
- Pitfalls: splitting behavior into frame slices requires explicit state (use State pattern or coroutines); order dependence (later objects see earlier ones' new state - use Double Buffer); modifying list during iteration (cache count, iterate backward, or mark dead and sweep after); dormant objects waste CPU - keep an active list; putting update on a base entity class creates brittle hierarchies - prefer components.

## 413. Component
- Intent: Let one entity span domains (input, physics, graphics, audio) without coupling them.
- Use when: A class touches multiple domains; class is too big; inheritance cannot pick exactly the reusable parts.
- Structure/how: Split monolith by domain into components; entity becomes a thin container calling them; swap implementations (player input vs AI input for demo mode); assemble entities via factory functions.
- Communication: shared container state (simple, order-dependent), direct references between closely related components (fast, coupled), messaging via container (decoupled, beware loops). Rule: share basic state, link close pairs directly, message for minor events.
- Pros: decoupled domains, reuse, can improve cache use. Cons: more objects to wire; extra indirection; update-order bugs.
- Related to / UI example: Entity-Component-System; UI composition and hooks; composition over inheritance.

## 414. Event Queue
- Intent: Decouple when a message is sent from when it is processed.
- Use when: Need to decouple timing (not just identity - for that, Observer/Command is simpler); not when sender needs an immediate response.
- Structure/how: FIFO ring buffer (fixed array, head/tail wrap with modulo, one slot left empty to distinguish full/empty); no per-item allocation; aggregate duplicate requests at enqueue; lock + condition variable for threads.
- Pitfalls: a central event bus is global state; stale data - capture needed data at send time since the entity may be gone; hidden feedback loops (avoid sending from handlers, log); aggregation window depends on queue size.
- Design decisions: events (past, many listeners) vs messages (future, one handler); single-cast vs broadcast vs work-queue; single vs multiple writers; message ownership (transfer, shared, pool).
- Related to / UI example: UI message queues/event loop, Redux action dispatch, audio request queues.

## 415. Service Locator
- Intent: Global access to a service without coupling to its concrete class or lookup.
- Use when: Sparingly - truly ambient singular systems (logging, audio, memory) where passing the object through layers clutters code.
- Structure/how: Service interface; concrete providers; locator holds current provider, registered at startup. Null Service default so callers never null-check (also mutes systems in dev). Decorated/logging provider wraps another to add logging per subsystem.
- Pitfalls: hidden runtime dependencies; temporal coupling (must register before use); providers must work from any context; null services can mask bugs; global access reduces control.
- Related to: Singleton (shares drawbacks), Dependency Injection (preferred when possible), Null Object, Decorator.

## 416. Dirty Flag
- Intent: Avoid redundant work by deferring recomputation of derived data until needed.
- Use when: Derived data is expensive; primary data changes more often than derived data is read; incremental update is impractical.
- Structure/how: Cache derived value plus a dirty bit; any change sets it; on read, recompute if dirty then clear. Scene graphs propagate "parent dirty" lazily during traversal.
- Pitfalls: stall when work runs on demand; deferred work lost on crash; every mutation path must set the flag (route changes through a narrow interface); memory for cache.
- Design decisions: clean on demand vs at checkpoints vs in background; fine vs coarse granularity.
- Related to / UI example: Virtual DOM/reconciliation dirty marking, layout invalidation (`invalidate()` then relayout), memoized selectors, unsaved-changes indicator.

## 417. Object Pool
- Intent: Reuse preallocated objects instead of repeated heap alloc/free, improving speed and avoiding fragmentation.
- Use when: Frequent create/destroy of similar-sized objects (particles, bullets, sounds); expensive resources (connections).
- Structure/how: Allocate block at startup; mark in-use; free list threaded through unused objects for O(1) acquire/release.
- Pitfalls: over/undersized pool; policy when full (prevent, skip, evict, grow); slot size fits largest object; reused objects keep stale data (fully reinitialize, debug-clear); pooled objects can keep GC references alive.
- Related to / UI example: Virtualized list row recycling (RecyclerView, UITableView cell reuse); Object cesspool anti-pattern if state not reset.

## 418. Spatial Partition
- Intent: Organize objects by position to find nearby ones without scanning all.
- Use when: Many positioned objects and frequent proximity queries are a bottleneck.
- Structure/how: Grid of cells with linked lists; move objects between cells as they move; check neighbor cells (half of them to avoid double counting).
- Pitfalls: update cost for moving objects; extra memory; cell size tuning; not worth it for small counts.
- Design decisions: flat (grid: simple, constant memory) vs hierarchical (handles density); fixed vs adaptive boundaries (BSP, k-d tree, BVH best for static geometry); quadtree/octree as middle ground; sole storage vs secondary index.
- Related to / UI example: Hit-testing in canvas/map apps, collision detection, viewport culling.

## 419. Double Buffer
- Intent: Make a sequence of incremental changes appear instantaneous to readers.
- Use when: State is modified incrementally, may be read mid-modification, readers must see only complete results without waiting.
- Structure/how: Current buffer (read) and next buffer (write); swap atomically when done. Also used for per-actor state to remove update-order dependence.
- Pitfalls: swap must be atomic and cheap; doubles memory; pointer swapping invalidates persistent pointers and yields data two frames old; copying is fresher but slower.
- Related to / UI example: Screen framebuffers, offscreen canvas rendering, React's work-in-progress vs current fiber trees, immutable next-state reducers.

## 420. Data Locality
- Intent: Arrange data contiguously in the order it is processed to exploit CPU caches.
- Use when: Profiling shows cache misses dominate a hot loop.
- Structure/how: Arrays of components instead of pointer-chasing; hot/cold splitting; sort active objects to front.
- Pitfalls: sacrifices abstraction (interfaces, pointers); premature use complicates code.
- Related to: Component pattern, ECS, structure-of-arrays.

## 421. Type Object
- Intent: Represent "kinds" of things as data objects instead of subclasses, so new types need no code.
- Use when: Many variants differ mainly in data (monster breeds); designers add types.
- Structure/how: Each instance references a Type object holding shared attributes; types can inherit from parent types; load from data files.
- Pitfalls: behavior is hard to express in data (combine with Bytecode or Strategy); manual type management.
- Related to: Prototype, Flyweight; UI example: schema-driven form fields.

## 422. Bytecode
- Intent: Encode behavior as instructions for a small virtual machine, giving data-driven, sandboxed behavior.
- Use when: Many behaviors need defining outside code; faster iteration or modding; safety.
- Structure/how: Instruction set + stack-based VM; authoring tool or compiler front end.
- Pitfalls: becomes a language you must maintain (debuggers, tooling); scope creep.
- Related to: Interpreter (slower tree-walking alternative).

## 423. Subclass Sandbox
- Intent: Base class provides protected primitive operations; subclasses implement behavior using only those.
- Use when: Many sibling behaviors with minimal coupling to the rest of the engine.
- Pitfalls: fragile base class; base becomes a dumping ground - push operations into separate providers.
- Related to: Template Method (inverse direction), Facade.

## 424. Observer (game revisited)
- Intent: Decouple achievement/audio systems from physics events.
- Pitfalls: synchronous - slow observers block the subject; dangling observers on destruction (lapsed listener); prefer Event Queue for async.

## 425. Command (game revisited)
- Intent: Map input buttons to command objects; actor-parameterized commands let AI and players share control; undo for editors/strategy games; replay recording.

## 426. Flyweight (game revisited)
- Intent: Share mesh/texture/terrain type data across thousands of instances; GPU instanced rendering is hardware flyweight.

## 427. Prototype (game revisited)
- Intent: Spawners clone a prototype monster; data-driven prototypes with delegation in JSON reduce duplication.

## 428. Singleton (game revisited)
- Verdict: Singletons are globals in disguise - encourage coupling, are concurrency-unfriendly, and lazy init can hitch frames. Alternatives: pass it in, get it from a base class, get it from an existing global (World), or Service Locator.

## 429. State (game revisited)
- Intent: Finite state machines for character controllers; enhancements: hierarchical states (shared superstate behavior), pushdown automata (stack for return-to-previous state), concurrent state machines (e.g., movement x equipment).
- Pitfalls: FSMs scale poorly for complex AI - consider behavior trees/planners.
- Related to / UI example: UI flows (wizards, modal stacks as pushdown automaton).

# Part 25 — Additional patterns from large catalogs (iluwatar/java-design-patterns and others)

## 430. Null Object / Special Case
- Intent: Provide a do-nothing object implementing the interface instead of null.
- Use when: Callers would otherwise null-check everywhere.
- Pitfalls: can hide missing-configuration bugs.
- Related to: Sentinel Object (Python), Null Service, Effective Java 43 (return empty collections).

## 431. Sentinel Object (Python)
- Intent: A unique marker object signals "no value given" when `None` is a legitimate value.
- Structure/how: `_MISSING = object()` as default arg; compare with `is`.

## 432. Global Object (Python)
- Intent: Module-level objects for constants and shared state, imported by name - the Pythonic replacement for Singleton.
- Pitfalls: mutable globals create hidden coupling; avoid I/O at import time.

## 433. Prebound Method (Python)
- Intent: Expose a bound method of a module-level instance as a module function (`random.random`-style), so callers use a simple function while state lives in an object.

## 434. Dependency Injection
- Intent: Supply an object's collaborators from outside rather than constructing them inside.
- Use when: Testability, swapping implementations, DIP.
- Structure/how: Constructor/setter/parameter injection; composition root or container.
- Pitfalls: container magic hides wiring; long constructor lists signal SRP violations.

## 435. Repository
- Intent: Collection-like interface over persistence that hides query details from the domain.
- Related to: DAO, Data Mapper, Unit of Work, Specification (composable query criteria).

## 436. Data Access Object (DAO) / Data Mapper / Active Record contrast
- Intent: DAO isolates CRUD for a table/entity; Data Mapper moves data between objects and DB keeping them ignorant of each other.
- Pitfalls: leaky abstractions over ORM; anemic models.

## 437. Unit of Work
- Intent: Track changed objects during a business transaction and commit them together.
- Related to: Identity Map (one in-memory instance per DB row).

## 438. Data Transfer Object (DTO) / Value Object
- Intent: DTO bundles data for transport across boundaries; Value Object is an immutable, equality-by-value domain type (Money, DateRange).
- Pitfalls: DTOs leaking into domain logic; primitive obsession when value objects are skipped.

## 439. Lazy Loading / Virtual Proxy
- Intent: Defer loading until first use.
- Pitfalls: N+1 queries; unexpected latency at access time.
- Related to / UI example: Code splitting, lazy images, infinite scroll.

## 440. Caching
- Intent: Store expensive results for reuse (cache-aside, write-through, write-behind).
- Pitfalls: invalidation, staleness, caching failures (see anti-pattern).

## 441. Circuit Breaker
- Intent: Stop calling a failing remote service after repeated failures; open -> half-open -> closed states.
- Related to: Retry (with backoff), Fallback, Bulkhead (isolate resource pools), Rate Limiting/Throttling, Health Check.
- UI example: Show degraded UI/cached data when backend breaker is open.

## 442. Retry
- Intent: Re-attempt transient failures with backoff and jitter.
- Pitfalls: retry storms; non-idempotent operations - pair with Idempotent Consumer.

## 443. Event Sourcing
- Intent: Store state as an append-only log of events and rebuild state by replay.
- Pros: audit, time travel. Cons: schema evolution, replay cost (snapshots).
- Related to: CQRS, Write-Ahead Log, Redux devtools time-travel.

## 444. CQRS
- Intent: Separate write model (commands) from read model (queries).
- Pitfalls: eventual consistency complexity; overkill for CRUD.

## 445. Saga / Transactional Outbox
- Intent: Saga coordinates a distributed transaction as local steps with compensating actions; Outbox writes events in the same DB transaction as state, then relays them reliably.

## 446. Layered / Hexagonal / Onion / Clean Architecture
- Intent: Organize code so domain logic sits at the center and depends on nothing external; adapters (UI, DB, HTTP) plug into ports.
- Pitfalls: ceremony for small apps; layering skipped in practice (Lasagna code if too many layers).

## 447. Anti-Corruption Layer
- Intent: Translate between your domain model and a legacy/external model so its concepts do not leak in.
- Related to: Adapter, Facade at system scale.

## 448. Strangler (Fig)
- Intent: Incrementally replace a legacy system by routing features to new code until the old can be removed.

## 449. Microservices supporting patterns
- API Gateway (single entry point), Backends for Frontends (per-client tailored API), Aggregator, Client-side UI composition (micro-frontends), Distributed tracing, Log aggregation, Self-registration, Messaging, Load shedding, Queue-based load leveling, Sharding, Leader election.
- Pitfalls: distributed-systems complexity; start with a Monolith until boundaries are clear.

## 450. Producer-Consumer / Thread Pool / Fork-Join / Master-Worker / Reactor / Active Object / Promise
- Intent: Concurrency patterns - decouple producing work from consuming it with a queue; reuse worker threads; split-and-join tasks; demultiplex I/O events to handlers; give objects their own thread with an async request queue; represent a future result.
- Related to / UI example: JS event loop is a Reactor; Promises/async-await for UI data loading; Web Workers as master-worker.
- Related concurrency guards: Balking (skip if not ready), Guarded Suspension (wait for condition), Double-Checked Locking (lazy init - error-prone), Monitor, Lockable Object, Thread-Specific Storage, Poison Pill (shutdown message), Optimistic Offline Lock / Version Number.

## 451. Flux / Unidirectional Data Flow / MVI / Bloc
- Intent: Actions -> dispatcher/reducer -> store -> view, a single direction of state change.
- Pros: predictable, debuggable state. Cons: boilerplate.
- Related to / UI example: Redux, Elm architecture, Flutter Bloc; combines Command (actions), Observer (store subscription), Memento (state history).

## 452. Presentation Model / Page Object / View Helper / Template View / Composite View / Front Controller / Page Controller
- Intent: Web/UI layer patterns - abstract view state from widgets; encapsulate a UI page for tests; move view logic into helpers; render via templates; assemble views from sub-views; one handler receives all requests vs one controller per page.
- Related to / UI example: Page Object for E2E tests (Playwright/Selenium); layout components as Composite View.

## 453. Fluent Interface / Step Builder / Parameter Object / Execute Around / RAII
- Intent: Chainable readable APIs; builder steps enforced by types; bundle many params into one object; wrap resource setup/teardown around a passed callback; tie resource lifetime to object scope (try-with-resources, `with`, `using`).

## 454. Feature Toggle
- Intent: Switch features on/off at runtime via config.
- Pitfalls: toggle debt - remove stale flags; combinatorial test paths.

## 455. Specification / Rule Engine / Filterer / Pipeline / Collection Pipeline / Intercepting Filter
- Intent: Composable predicates; externalized rules; chained processing stages.
- Related to: Chain of Responsibility, Strategy, functional composition.

## 456. Functional patterns: Currying / Function Composition / Combinator / Monad / Trampoline
- Intent: Build behavior from small functions; chain computations with context (Optional, Promise); convert deep recursion into a loop.

## 457. Delegation / Extension Objects / Role Object / Twin / Private Class Data / Abstract Document
- Intent: Composition-based reuse and runtime extension - forward to a helper, attach interfaces dynamically, give objects context-specific roles, emulate multiple inheritance with paired objects, isolate data from behavior, model flexible property bags.

## 458. Registry / Multiton / Monostate / Marker Interface / Money / Converter / Tolerant Reader / Serialized LOB / Single Table Inheritance
- Brief: global lookup by key; one instance per key; all instances share state; type-tag interface; value type for currency; mapping between representations; read only needed fields so schema changes do not break clients; store object graph in one column; map hierarchy to one table.

## 459. Arrange-Act-Assert / Object Mother / Service Stub
- Intent: Testing patterns - structure tests in three phases; factory for canned test fixtures; replace a slow service with a stub.

# Part 26 — Anti-patterns

## 460. Code smells (refactoring.guru taxonomy)
- Intent: Surface symptoms that a refactoring is needed.
- Bloaters: Long Method, Large Class, Primitive Obsession, Long Parameter List, Data Clumps.
- Object-orientation abusers: Switch Statements (use polymorphism/Strategy/State), Temporary Field, Refused Bequest (LSP), Alternative Classes with Different Interfaces.
- Change preventers: Divergent Change (SRP), Shotgun Surgery, Parallel Inheritance Hierarchies (Bridge).
- Dispensables: excessive Comments, Duplicate Code, Lazy Class, Data Class, Dead Code, Speculative Generality.
- Couplers: Feature Envy (move method), Inappropriate Intimacy, Message Chains (Law of Demeter), Middle Man.
- Fix families: composing methods (Extract Method), moving features between objects, organizing data, simplifying conditionals, simplifying method calls, dealing with generalization.

## 461. Software development anti-patterns

## 462. The Blob / God Object
- Symptoms: one class holds most data and logic; others are data holders.
- Causes: procedural design in OO clothing; incremental feature dumping.
- Refactor: split by responsibility; move behavior to the data it uses.
- UI example: a single 3,000-line page component or "AppController".

## 463. Lava Flow
- Symptoms: dead or obscure code kept because nobody dares remove it.
- Refactor: tests first, then delete; architecture review; version control preserves history.

## 464. Poltergeists
- Symptoms: short-lived classes that only pass data or invoke others ("manager", "controller" stubs).
- Refactor: remove them and move behavior to collaborators.

## 465. Golden Hammer
- Symptoms: one familiar tool/pattern applied to every problem.
- Refactor: evaluate alternatives per problem; broaden team skills.

## 466. Spaghetti Code
- Symptoms: tangled control flow, little structure, global state.
- Refactor: modularize, extract functions, simplify flow.

## 467. Cut-and-Paste Programming
- Symptoms: duplicated code with small edits; bugs fixed in one copy only.
- Refactor: extract reusable abstractions (DRY).

## 468. Boat Anchor
- Symptoms: unused components/hardware retained for possible future use.
- Refactor: remove them.

## 469. Dead End
- Symptoms: modified third-party component that can no longer be upgraded.
- Refactor: isolate customizations behind adapters; contribute upstream.

## 470. Functional Decomposition
- Symptoms: OO system structured as procedural main routine plus subroutine classes.
- Refactor: redesign around domain objects with behavior.

## 471. Continuous Obsolescence
- Symptoms: tech changes faster than the team can integrate.
- Refactor: depend on stable open standards and isolation layers.

## 472. Input Kludge
- Symptoms: ad hoc input handling fails on unexpected input.
- Refactor: validate/sanitize at boundaries; use proper parsers.

## 473. Walking through a Minefield
- Symptoms: released software riddled with latent bugs.
- Refactor: proper testing and inspection.

## 474. Mushroom Management (development variant)
- Symptoms: developers isolated from end users and requirements.
- Refactor: user involvement, prototyping, feedback loops.

## 475. Error Hiding / Swallowed Exceptions
- Refactor: handle or propagate with meaningful messages and stack traces.

## 476. Magic Numbers / Magic Strings / Hard Code / Soft Code
- Refactor: named constants and enums; config for environment settings; keep business logic in code, not config.

## 477. Cargo Cult Programming / Programming by Permutation
- Symptoms: patterns or code used without understanding; random changes until it works.
- Refactor: learn the rationale; hypothesis-driven debugging.

## 478. Premature Optimization / Busy Waiting / Caching Failure
- Refactor: profile first; use events/blocking primitives; expire and invalidate cached errors.

## 479. Action at a Distance / Sequential Coupling / Object Cesspool / Shooting the Messenger
- Refactor: explicit dependencies, minimal globals; builders or APIs that prevent invalid call order; reset pooled state; isolate subscriber failures so one listener cannot break the publisher.

## 480. Not Invented Here / Reinventing the (Square) Wheel / Silver Bullet
- Refactor: adopt vetted libraries; benchmark alternatives; fix the underlying process, not just tooling.

## 481. Dependency Hell (DLL/JAR hell)
- Refactor: lock files, semantic versioning, isolation.

## 482. Software architecture anti-patterns

## 483. Stovepipe System / Stovepipe Enterprise
- Symptoms: subsystems integrated ad hoc with point-to-point links; each department builds isolated systems.
- Refactor: common interfaces/abstraction layer; enterprise architecture standards.

## 484. Vendor Lock-In
- Refactor: isolation layer, open standards, exit plan.

## 485. Architecture by Implication
- Symptoms: no documented architecture because "we've done this before".
- Refactor: explicit architecture plan addressing risks.

## 486. Reinvent the Wheel (architecture) / Wolf Ticket
- Symptoms: building from scratch despite existing designs; buying products that claim standards compliance they lack.
- Refactor: architecture mining of legacy/other systems; verify compliance and isolate with adapters.

## 487. Design by Committee / Swiss Army Knife
- Symptoms: overly complex designs from consensus; interfaces with every possible method.
- Refactor: one accountable architect; focused interfaces (ISP).

## 488. Big Ball of Mud
- Refactor: introduce modules with explicit boundaries; incremental refactoring.

## 489. Jumble / Cover Your Assets / Spaghetti architecture
- Symptoms: horizontal and vertical design elements mixed; documents that avoid decisions.
- Refactor: separate stable horizontal frameworks from vertical domain parts; make decisions explicit.

## 490. Inner-Platform Effect / Abstraction Inversion / Interface Bloat
- Refactor: use platform features; expose needed primitives; split interfaces.

## 491. Database-as-IPC / Race Hazard / Magic Pushbutton
- Refactor: use real messaging; synchronization and idempotency; move logic out of UI event handlers and add validation.
- UI example: Magic Pushbutton - all business logic inside a button click handler.

## 492. Anemic Domain Model / Call Super / Circular Dependency / Yo-yo Problem / Constant Interface / Object Orgy
- Refactor: put behavior in domain objects; Template Method; dependency inversion or extract shared module; flatten hierarchies and favor composition; enums/constant classes; encapsulate.

## 493. Software project management anti-patterns

## 494. Analysis Paralysis
- Symptoms: endless analysis, never committing.
- Refactor: time-box; incremental/iterative development.

## 495. Death by Planning
- Symptoms: excessive planning, plans maintained instead of software delivered.
- Refactor: plan around deliverables and milestones; keep plans lightweight.

## 496. Death March
- Refactor: honest risk assessment, scope cuts, or cancellation.

## 497. Corncob / Irrational Management / Smoke and Mirrors / Throw It Over the Wall / Fire Drill / Viewgraph Engineering / Project Mismanagement / Intellectual Violence
- Brief: disruptive individuals; indecisive or emotional management; demoing unfinished work as done; handing off without guidance; months of idleness then panic; staff stuck making slides; missing risk management; using jargon to silence others.
- Refactor: clear roles and accountability; decision processes; demo only working features; real-world prototyping; open technical discussion.

## 498. Bicycle Shed (Bikeshedding) / Groupthink / Escalation of Commitment / Micromanagement / Seagull Management / Mushroom Management
- Refactor: delegate trivia and time-limit decisions; devil's advocate; predefined kill criteria; set outcomes and trust teams; regular engagement; transparent communication.

## 499. Scope Creep / Gold Plating / Overengineering / Ninety-Ninety Rule / Brooks's Law / Bleeding Edge / Cart Before the Horse
- Refactor: baseline scope with change control; definition of done; build to current requirements; explicit remaining-work estimates with buffer; small teams and planned onboarding; prototype unproven tech; sequence by dependencies.

# Part 27 — Architectural styles

## 500. Layered (n-tier)
- Intent: separate concerns into presentation, application/service, domain, and data layers; each layer depends only on the one below.
- Use when: standard business/CRUD apps, teams split by skill; clear maintainability goals.
- How: requests flow top-down; strict (only adjacent) or relaxed layering.
- Trade-offs: easy to understand and test per layer; pitfalls are "sinkhole" layers that only pass calls through, cross-layer changes for every feature, and monolithic deployment.

## 501. Client-server
- Intent: centralize a service that many clients request.
- Use when: shared resources (email, banking, file servers).
- Trade-offs: server is a bottleneck/single point of failure; clients depend on network availability.

## 502. Master-slave (primary-replica)
- Intent: a primary distributes work to identical replicas and aggregates results; or replicates data to read copies.
- Use when: parallel computation, DB read replication.
- Trade-offs: primary is SPOF and bottleneck; replication lag; only works for decomposable problems.

## 503. Pipe-filter
- Intent: process a stream of data through independent filters connected by pipes.
- Use when: compilers, ETL, media/signal processing, Unix pipelines.
- Trade-offs: reusable, concurrent filters; slowest filter limits throughput; data-transformation overhead; hard to handle errors and interactive flows.

## 504. Broker
- Intent: decouple distributed components through an intermediary that routes requests.
- Use when: message brokers (Kafka, RabbitMQ), CORBA-style middleware.
- Trade-offs: location transparency and dynamic change; added latency, broker as SPOF, harder end-to-end debugging.

## 505. Peer-to-peer
- Intent: peers act as both clients and servers; roles change dynamically.
- Use when: file sharing, blockchain, some streaming.
- Trade-offs: highly scalable and robust; no guarantees on quality of service, security, or availability; performance depends on peer count.

## 506. Event-bus / event-driven
- Intent: producers publish events onto channels; subscribers react asynchronously.
- Use when: notification systems, UIs, loosely coupled integrations.
- Trade-offs: easy to add consumers; scalability limits when all messages flow through one bus; hard to reason about ordering, causality, and end-to-end flows.

## 507. Model-View-Controller
- Intent: split UI into model (state/logic), view (rendering), controller (input).
- Use when: web/desktop UIs with multiple views of the same data.
- Trade-offs: multiple views, separation of concerns; added complexity and possible unnecessary updates for simple UIs.

## 508. Blackboard
- Intent: specialized knowledge sources iteratively contribute partial solutions to a shared store; control component chooses next contributor.
- Use when: speech recognition, signal interpretation, problems without deterministic algorithms.
- Trade-offs: easy to add sources; hard to test, no guaranteed good solution, synchronization overhead.

## 509. Interpreter
- Intent: evaluate sentences of a language/DSL.
- Use when: query languages, rules engines, scripting.
- Trade-offs: highly dynamic, end-user programmable; slower than compiled code.

## 510. Microkernel (plug-in)
- Intent: minimal core plus independently developed plug-ins.
- Use when: IDEs, browsers, product platforms with variants.
- Trade-offs: extensibility and isolation; plug-in contract versioning and core stability are critical.

## 511. Monolith (microservices.io)
- Intent: single deployable unit.
- Use when: early-stage product, small team, unclear domain boundaries.
- Trade-offs: simple to develop, test, deploy; scaling, tech lock-in, slow builds and coordinated releases as it grows. Prefer a modular monolith before splitting.

## 512. Microservice architecture
- Intent: independently deployable, loosely coupled services owned by small teams, organized around business capabilities.
- Use when: large/complex apps needing independent deployability, scaling, team autonomy.
- Trade-offs: distributed-system complexity (network failure, data consistency, observability), operational overhead, need for automation (CI/CD, platform).

# Part 28 — Enterprise application patterns (Fowler PoEAA)

## 513. Transaction Script
- Intent: one procedure per request containing all business logic.
- Use when: simple logic, few rules.
- Pitfalls: duplication grows as logic gets complex; becomes unmaintainable.

## 514. Domain Model
- Intent: object model combining data and behavior.
- Use when: complex, changing business rules.
- Pitfalls: needs Data Mapper for persistence; higher learning curve; overkill for CRUD.

## 515. Table Module
- Intent: one instance handles logic for all rows of a table; works with Record Sets.
- Use when: platforms with strong record-set tooling (.NET DataSet).
- Pitfalls: weak at modelling complex object relations.

## 516. Service Layer
- Intent: defines application boundary operations; coordinates transactions, security and responses over the domain.
- Use when: multiple client types or integration gateways share the logic.
- Pitfalls: anemic domain if all logic migrates into services; keep it thin.

## 517. Table Data Gateway / Row Data Gateway
- Intent: one object per table (TDG) or per row (RDG) encapsulating SQL.
- Use when: Transaction Script/Table Module designs.
- Pitfalls: RDG mixes poorly with complex domain logic; logic leaks toward Active Record.

## 518. Active Record
- Intent: object wraps a row and carries persistence + domain logic.
- Use when: domain objects map ~1:1 to tables; simple logic (Rails, many ORMs).
- Pitfalls: couples domain to schema; hard with inheritance, complex mapping and testing without DB.

## 519. Data Mapper
- Intent: separate mapper layer moves data between objects and DB, keeping them independent.
- Use when: rich Domain Model with schema divergence.
- Pitfalls: extra layer of complexity; usually use an ORM rather than hand-rolling.

## 520. Unit of Work
- Intent: track changed objects in a business transaction and commit them together, resolving concurrency.
- Pitfalls: long-lived units hold stale data; must pair with locking strategy.

## 521. Identity Map
- Intent: ensure each object is loaded once per session; lookup by key before DB.
- Pitfalls: scope to a session/transaction, not global (memory, staleness).

## 522. Lazy Load
- Intent: defer loading until needed (lazy init, virtual proxy, value holder, ghost).
- Pitfalls: N+1 query ripple loading; identity problems with proxies; loads outside open session fail.

## 523. Identity Field / Foreign Key Mapping / Association Table Mapping / Dependent Mapping / Embedded Value / Serialized LOB
- Identity Field: keep DB key in object; prefer meaningless surrogate keys.
- Foreign Key Mapping: map 1:N references to FK columns.
- Association Table Mapping: link table for M:N.
- Dependent Mapping: parent mapper persists children with no own identity.
- Embedded Value: map value objects (Money, DateRange) into owner's columns.
- Serialized LOB: store object graph in one column; pitfalls are no querying inside, versioning of serialized format.

## 524. Single / Class / Concrete Table Inheritance; Inheritance Mappers
- Single Table: one table for hierarchy; simple, no joins; wasted nullable columns, wide tables.
- Class Table: table per class; normalized; joins per load, hot base table.
- Concrete Table: table per concrete class; no joins; key uniqueness across tables and refactoring superclass fields are painful.
- Inheritance Mappers: organize mapper hierarchy to mirror domain hierarchy.

## 525. Metadata Mapping / Query Object / Repository
- Metadata Mapping: mapping in config/annotations; reduces boilerplate, harder to debug.
- Query Object: build queries as objects in domain terms; decouples from SQL dialect.
- Repository: collection-like interface over mapping layer; isolates domain from persistence and centralizes queries. Pitfall: generic repositories that leak query semantics (IQueryable) defeat the purpose.

## 526. Model View Controller / Page Controller / Front Controller / Application Controller
- Page Controller: one handler per page/action; simple sites.
- Front Controller: single entry handler dispatches commands; centralizes security, i18n, logging.
- Application Controller: centralizes screen flow/navigation in complex wizards.

## 527. Template View / Transform View / Two Step View
- Template View: markers in HTML filled at render; keep logic out of templates.
- Transform View: element-by-element transform (XSLT style).
- Two Step View: produce logical page then render to HTML; enables global look changes and multiple skins.

## 528. Remote Facade
- Intent: coarse-grained interface over fine-grained objects to minimize remote calls.
- Rule: never expose fine-grained domain objects across a network boundary; one call per use case.

## 529. Data Transfer Object
- Intent: serializable carrier for data across process boundary.
- Pitfalls: DTO explosion, duplicating domain; don't use for in-process layering without need.

## 530. Optimistic Offline Lock
- Intent: detect conflicts at commit using version numbers; roll back losing transaction.
- Use when: low contention.
- Pitfalls: users lose work on conflict; must check version on every update path.

## 531. Pessimistic Offline Lock / Coarse-Grained Lock / Implicit Lock
- Pessimistic: acquire lock before editing; use when conflicts are frequent/costly; needs lock timeouts and lock manager; reduces concurrency.
- Coarse-Grained: one lock for an aggregate of related objects (shared version).
- Implicit Lock: framework/supertype acquires locks so developers can't forget.

## 532. Client / Server / Database Session State
- Client: state in cookie/URL/hidden fields; scales horizontally; size limits, must sign/encrypt and never trust.
- Server: in-memory or serialized on server; simple; needs sticky sessions or replication.
- Database: committed rows; stateless app servers; extra DB load and cleanup of abandoned sessions.

## 533. Base patterns (Gateway, Service Stub, Record Set, Mapper, Layer Supertype, Separated Interface, Registry, Value Object, Money, Special Case, Plugin)
- Gateway: wrap each external system/API in one object; swap for Service Stub in tests.
- Separated Interface + Plugin: declare interface in one package, bind implementation by configuration (dependency inversion).
- Registry: well-known lookup for shared services; prefer DI to avoid hidden global state.
- Value Object: immutable, equality by value; Money: amount + currency, handle rounding and allocation explicitly (never floats).
- Special Case (Null Object): subclass for missing/unknown case removes null checks.
- Layer Supertype: common base for a layer (e.g., ID handling).

# Part 29 — Distributed systems patterns (Patterns of Distributed Systems)

## 534. Write-Ahead Log
- Intent: durability without flushing data structures on every change.
- How: append each state change as a command to a log, fsync, then apply; replay on restart.
- Pitfalls: fsync cost (batch flushes); log growth needs Segmented Log + Low-Water Mark; duplicate detection on replay.

## 535. Segmented Log
- Split log into segment files for easier cleanup/rolling; pitfalls are many open files and index lookup across segments.

## 536. Low-Water Mark
- Track index below which log entries can be discarded (snapshot- or time-based).

## 537. High-Water Mark
- Index of last entry replicated to a quorum; only entries below it are visible to clients; followers truncate uncommitted entries above it after leader change.

## 538. Leader and Followers
- One leader orders and replicates writes; followers apply. Pitfalls: leader bottleneck, election downtime, split brain (use Generation Clock + quorum).

## 539. HeartBeat
- Periodic liveness signal; timeouts must exceed network jitter/GC pauses to avoid false failure detection; interval is a trade-off between detection speed and noise.

## 540. Majority Quorum
- Decision needs majority (n/2+1); tolerates f failures with 2f+1 nodes. Pitfalls: larger clusters slow writes; even-sized clusters waste a node.

## 541. Generation Clock (epoch / term)
- Monotonic number per leadership term; reject requests with older generation to fence stale leaders (zombies).

## 542. Paxos
- Two-phase (prepare/accept) consensus safe under partitions; liveness issues with dueling proposers; prefer Raft-style replicated log in practice.

## 543. Replicated Log
- Replicate WAL entries in same order on all nodes (Raft, Multi-Paxos) to get identical state machines. Requires leader, quorum, high-water mark.

## 544. Singular Update Queue
- Single thread consumes a queue of updates; avoids locks while preserving order; caller gets future/async response. Pitfall: queue backlog needs bounded size/backpressure.

## 545. Request Waiting List
- Track pending client requests awaiting quorum responses; complete or time out each.

## 546. Idempotent Receiver
- Unique client ID + request sequence; server stores responses and returns cached result for duplicates. Pitfall: expiring saved results safely.

## 547. Follower Reads
- Serve reads from replicas to scale reads/reduce latency; risk stale reads; use read-your-writes via version tracking, or nearest-replica routing.

## 548. Versioned Value
- Store every update as a new version; enables MVCC, snapshot reads; needs garbage collection of old versions.

## 549. Version Vector
- Per-node counters detect concurrent updates (siblings) in leaderless stores; app or CRDT must resolve conflicts; vector size grows with node count.

## 550. Fixed Partitions
- Pre-create many more partitions than nodes; map keys to partitions by hash; move whole partitions on resize so key->partition never changes. Pick partition count up front carefully.

## 551. Key-Range Partitions
- Sorted ranges enable range scans; split ranges as they grow; pitfall: hot ranges (sequential keys like timestamps).

## 552. Two-Phase Commit
- Prepare then commit across participants for atomicity; coordinator failure blocks participants holding locks; high latency; avoid across microservices (use Saga).

## 553. Lamport Clock
- Logical counter for partial ordering; doesn't capture concurrency; ties broken by node ID.

## 554. Hybrid Clock
- Wall-clock + logical counter: monotonic, ordered, human-readable timestamps (HLC). Still bounded by clock skew assumptions.

## 555. Clock-Bound Wait
- Wait out max clock uncertainty before commit/read so timestamps are globally ordered (Spanner TrueTime). Needs tight clock sync; adds latency.

## 556. Lease
- Time-bound rights that expire automatically; avoids indefinite locks when holder dies. Pitfall: clock drift; holder must stop acting before expiry (use monotonic clocks, fencing tokens).

## 557. State Watch
- Clients register watches on keys and are notified of changes (ZooKeeper/etcd). Must handle missed events on reconnect (resume from version).

## 558. Gossip Dissemination
- Each node periodically shares state with random peers; converges in O(log n) rounds; eventually consistent membership/metadata; bandwidth bounded.

## 559. Emergent Leader
- Oldest member in membership list acts as coordinator without election; pitfall: split brain under partitions.

## 560. Consistent Core
- Small Raft/ZooKeeper cluster provides linearizable metadata, leases, membership for a large data cluster that can't run consensus at scale.

## 561. Single-Socket Channel
- One TCP connection per peer preserves ordering; pitfall: head-of-line blocking; combine with pipelining.

## 562. Request Batch / Request Pipeline
- Batch: combine small requests to improve throughput (tune max size + linger time vs latency).
- Pipeline: send multiple requests without waiting for responses; bound in-flight requests to avoid overload.

# Part 30 — System design fundamentals (system-design-primer)

## 563. Performance vs scalability
- Performance problem: slow for a single user. Scalability problem: fast for one, slow under load.
- Rule: a scalable service gains capacity proportional to resources added.

## 564. Latency vs throughput
- Aim for maximal throughput with acceptable latency; measure tail percentiles, not averages.

## 565. CAP theorem
- Under network partition choose Consistency or Availability; partition tolerance is not optional in networks.
- CP: may error/time out; use for atomic reads/writes (payments, inventory). AP: may return stale data; use when eventual consistency is OK.

## 566. Consistency patterns (weak, eventual, strong)
- Weak: reads may never see a write (VoIP, games, memcached).
- Eventual: async replication, converges in ms (DNS, email, Dynamo-style stores); handle stale reads.
- Strong: sync replication; reads see latest write (RDBMS, file systems); higher write latency and lower availability.

## 567. Availability patterns: fail-over
- Active-passive: heartbeat; standby takes over IP; hot vs cold standby determines downtime; risk of losing unreplicated writes.
- Active-active: both serve traffic; clients/DNS must know both; conflict handling for writes.
- Pitfalls: more hardware and complexity; data loss window.

## 568. Availability in numbers
- Sequence: A = A1 x A2 (availability drops). Parallel: A = 1 - (1-A1)(1-A2) (rises).
- 99.9% ~ 8h45m/year downtime; 99.99% ~ 52m/year. Every serial dependency costs nines.

## 569. DNS
- Hierarchical name resolution cached by TTL; records A, CNAME, NS, MX.
- Routing: weighted round robin, latency-based, geolocation.
- Pitfalls: propagation delay/stale caches, lookup latency, DDoS target; keep TTLs low before migrations.

## 570. CDN (push vs pull)
- Push: upload on change; good for low-traffic or rarely changing content; you manage expiry; more storage.
- Pull: fetched on first request then cached for TTL; less storage; first-request latency; redundant refetches if TTL < change rate.
- Pitfalls: cost, stale content until TTL/purge; need URL versioning (cache busting).

## 571. Load balancer
- Distributes traffic, removes unhealthy nodes, can terminate TLS and handle session persistence.
- Algorithms: random, round robin (weighted), least connections/least loaded, session/cookie hash.
- L4: by IP/port, fast, cheap. L7: by headers/path/cookies, more flexible, more CPU.
- Pitfalls: LB as bottleneck/SPOF (run active-passive/active-active pairs); added complexity.

## 572. Horizontal scaling
- Prefer stateless commodity servers; move sessions to shared store (Redis/DB); downstream (DB, cache) must handle more connections.

## 573. Reverse proxy
- Single front for internal services: hides backends, IP blocking, connection limits, TLS termination, compression, caching, static serving.
- Useful even with one server; pitfall: SPOF unless redundant.

## 574. Application layer separation & service discovery
- Split web and app tiers to scale independently; microservices register in a registry (Consul, etcd, ZooKeeper) with health checks.

## 575. RDBMS replication (master-slave, master-master)
- Master-slave: writes to primary, reads from replicas; promotion logic needed; replication lag; data loss if primary dies before replicating.
- Master-master: both accept writes; needs routing + conflict resolution; trade-off between loose consistency and synchronous write latency.

## 576. Federation (functional partitioning)
- Split DBs by function (users, products); smaller DBs, more cache hits; pitfalls: cross-DB joins, app routing, not a fix for one huge table.

## 577. Sharding
- Distribute rows across DBs by key; pitfalls: complex app logic, cross-shard joins, hot shards (celebrity users), rebalancing (use consistent hashing).

## 578. Denormalization
- Duplicate data to avoid joins and speed reads; pitfalls: duplicate writes, harder constraints, worse under heavy writes; often use materialized views.

## 579. SQL tuning
- Benchmark (load-test) and profile (slow query log) before tuning.
- Tight schema: CHAR for fixed-length, VARCHAR otherwise, DECIMAL for money, INT for counters; avoid large BLOBs (store references to object storage); NOT NULL where possible.
- Index columns used in WHERE/ORDER BY/GROUP BY/JOIN; indexes cost writes and memory; drop indexes during bulk load if appropriate.
- Avoid expensive joins; partition tables (hot vs cold); beware query cache contention.

## 580. NoSQL types
- Key-value: O(1) access, simple, fast; complexity moves to app.
- Document: flexible schema, query by fields; weak at relational joins.
- Wide column: column families, massive scale and availability (Bigtable, HBase, Cassandra).
- Graph: many-to-many relationships; less tooling.
- BASE: basically available, soft state, eventual consistency.

## 581. SQL vs NoSQL selection
- SQL: structured relational data, strict schema, joins, transactions, mature tooling, index lookups.
- NoSQL: semi-structured/dynamic schema, non-relational, very high throughput/TB-PB data, no complex joins.
- Pitfall: choosing NoSQL without a scale/schema need and losing transactions later.

## 582. Caching layers
- Client, CDN, web server/reverse proxy, database internal cache, application cache (Redis/Memcached, LRU).
- Query-level caching: key = hash of query; hard to invalidate. Object-level caching: cache assembled objects; invalidate on underlying change; preferred.
- Avoid file-based local caches (break cloning/autoscaling).
- What to cache: sessions, rendered pages, activity streams, user graph data.

## 583. Cache update strategies
- Cache-aside: app reads cache, on miss reads DB and fills; only requested data cached; pitfalls: 3 trips on miss, staleness (TTL), cold cache on node replacement.
- Write-through: write to cache which writes to DB synchronously; reads fast, writes slower; much written data never read (TTL); new nodes empty.
- Write-behind (write-back): write to cache, async to DB; fast writes; data loss if cache fails; complex.
- Refresh-ahead: refresh hot entries before expiry; poor prediction wastes work and can hurt performance.
- General pitfalls: consistency between cache and source (invalidation is hard), thundering herd on expiry.

## 584. Asynchronism: message queues, task queues
- Queues receive, hold and deliver messages; workers process later; clients get fast acknowledgement.
- Options: Redis (simple, may lose messages), RabbitMQ (AMQP, self-managed), SQS (hosted, higher latency, at-least-once/duplicates).
- Task queues (Celery): run computationally heavy jobs in background with scheduling.

## 585. Back pressure
- Bound queue size; when full, reject with HTTP 503 so clients retry with exponential backoff; protects latency.
- Pitfall: async adds latency/complexity; cheap or real-time operations may be better synchronous.

## 586. Communication: TCP, UDP
- TCP: reliable, ordered, congestion control; higher latency; use pooling for many connections; use when correctness > timeliness (web, DB, file transfer).
- UDP: connectionless, unordered, lossy, low latency; use for VoIP, video, games, DHCP; when late data is worse than lost data.

## 587. Communication: RPC vs REST
- RPC (gRPC, Thrift): looks like local call, efficient, internal APIs; tightly coupled, new API per operation, hard to debug/cache.
- REST: stateless resource-oriented over HTTP verbs; cacheable, good for public APIs and horizontal scaling; pitfalls: poor fit for non-hierarchical resources, many round-trips for nested data (mobile), limited verbs.

## 588. Back-of-envelope numbers
- Know latency orders of magnitude (L1 ~1ns, RAM ~100ns, SSD random read ~150us, datacenter RTT ~0.5ms, cross-continent ~150ms) and powers of two to size systems.

# Part 31 — Cloud design patterns (Azure Architecture Center)

## 589. Ambassador
- Intent: out-of-process helper (proxy) that makes network calls on behalf of a service: retries, circuit breaking, monitoring, routing, TLS.
- Use when: legacy or polyglot apps that can't be modified; standardize client connectivity.
- Trade-offs: extra hop latency; not for latency-critical paths; deploy as sidecar per instance or shared; must handle idempotency of retried calls.

## 590. Anti-Corruption Layer
- Intent: translation façade between a new system and a legacy/external system so legacy semantics don't pollute the new model.
- Use when: migrations over time, integrating systems with different semantics.
- Trade-offs: added latency; extra service to scale and operate; decide whether it's permanent or retired after migration; keep transactional/consistency semantics explicit.

## 591. Asynchronous Request-Reply
- Intent: backend work is long-running but client needs prompt response.
- How: API returns HTTP 202 Accepted with a status endpoint (Location header); client polls; on completion returns 302/200 with resource URL; optional Retry-After.
- Pitfalls: not all clients support polling (consider webhooks/websockets); need status-store cleanup; handle cancellation and idempotency.

## 592. Backends for Frontends
- Intent: separate backend per client type (web, mobile, partner) tailored to its needs.
- Use when: client requirements diverge significantly; teams own each frontend end-to-end.
- Trade-offs: code duplication across BFFs; more services to deploy; avoid if all clients need the same API.

## 593. Bulkhead
- Intent: partition resources (connection pools, threads, service instances, consumers) so a failure in one area doesn't exhaust all.
- Use when: protecting critical consumers, isolating noisy tenants or failing dependencies.
- Trade-offs: less efficient resource use; choose granularity carefully; combine with retry, circuit breaker, throttling; monitor each partition.

## 594. Cache-Aside
- Intent: load data on demand into a cache; app manages it.
- How: read cache; on miss read store and populate; on update write store then invalidate cache entry.
- Pitfalls: choose expiration to match access patterns; eviction policy; prime cache optionally; stale data and race conditions between update and invalidate; not ideal for static data sets that fit in memory or as session store in web farms.

## 595. Choreography
- Intent: services react to events and decide their own steps without central orchestrator.
- Use when: simple workflows, independently evolving services, avoiding orchestrator bottleneck.
- Trade-offs: hard to see/monitor overall flow; cyclic dependencies; failure handling distributed; becomes messy as steps grow (switch to orchestration).

## 596. Circuit Breaker
- Intent: stop calling a failing remote dependency to fail fast and let it recover.
- How: Closed (counting failures) -> Open after threshold (fail immediately, timer) -> Half-Open (allow trial requests) -> Closed on success.
- Pitfalls: tune thresholds per dependency; distinguish error types (timeouts vs 4xx); provide fallbacks; log state changes; per-resource breakers (not one global); don't use for local in-process resources; combine with Retry carefully (retry should respect open circuit).

## 597. Claim Check
- Intent: store large payload in external storage; send only a reference token through the bus.
- Trade-offs: extra storage operations and latency; lifecycle/cleanup of stored payloads; secure the storage reference.

## 598. Compensating Transaction
- Intent: undo completed steps of an eventually consistent multi-step operation.
- How: record steps; on failure run application-specific compensations (not simple rollbacks), possibly in reverse order.
- Pitfalls: compensations must be idempotent and retryable; data may have changed since; system may be inconsistent during compensation; may need manual intervention.

## 599. Competing Consumers
- Intent: multiple consumers read from one queue to scale and balance load.
- Pitfalls: message ordering is not guaranteed; consumers must be idempotent; poison messages need dead-letter handling; return results via separate reply channel; queue itself can be bottleneck.

## 600. Compute Resource Consolidation
- Intent: combine multiple tasks into one computational unit to raise utilization and cut cost.
- Pitfalls: noisy neighbors; scaling all together; fault isolation reduced; group only tasks with similar scalability, lifetime, and security profiles.

## 601. CQRS
- Intent: separate write model (commands) from read model (queries).
- Use when: read/write loads differ greatly, complex domains, collaborative domains, combined with event sourcing.
- Trade-offs: complexity; eventual consistency between write and read stores; messaging failures/duplicates; avoid for simple CRUD.

## 602. Deployment Stamps
- Intent: deploy multiple independent copies (scale units) of the full stack, each serving a subset of tenants/regions.
- Trade-offs: deployment automation needed; cross-stamp data aggregation is hard; tenant routing layer; capacity planning per stamp.

## 603. Event Sourcing
- Intent: persist state as an append-only sequence of events; current state derived by replay.
- Use when: audit history, temporal queries, complex domains, with CQRS read models.
- Trade-offs: eventual consistency of projections; event schema versioning; snapshots for long streams; hard to delete data (GDPR); querying requires projections; ordering and idempotency across consumers.

## 604. External Configuration Store
- Intent: move config out of deployment packages into a central store.
- Pitfalls: store availability is critical (cache locally); secure secrets separately (key vault); versioning and change propagation; schema validation.

## 605. Federated Identity
- Intent: delegate authentication to an external identity provider (claims-based, SSO).
- Pitfalls: IdP is a single point of failure (multi-region); claim mapping and authorization still in app; home realm discovery for multiple IdPs.

## 606. Gatekeeper
- Intent: dedicated host validates and sanitizes requests before forwarding to trusted backends with minimal privileges.
- Pitfalls: extra hop latency; gatekeeper must not hold keys/credentials; can be bottleneck/SPOF (scale out); use only internal secure channels behind it.

## 607. Gateway Aggregation
- Intent: gateway fans out to multiple backends and returns a combined response to reduce chattiness.
- Pitfalls: gateway latency and failures; avoid coupling business logic into gateway; handle partial failures; use async I/O and timeouts.

## 608. Gateway Offloading
- Intent: offload cross-cutting concerns (TLS termination, auth, rate limiting, logging, compression) to gateway.
- Pitfalls: don't offload business logic; gateway must be highly available and scalable.

## 609. Gateway Routing
- Intent: single endpoint routes requests by path/header to backend services or versions.
- Use when: simplifying clients, versioning, blue/green and canary.
- Pitfalls: gateway SPOF/bottleneck; keep routing config simple and fast.

## 610. Geode
- Intent: deploy full backend instances in many regions, each able to serve any request, with globally replicated data.
- Pitfalls: needs multi-master replicated data store; eventual consistency; cost; deploy and monitor uniformly.

## 611. Health Endpoint Monitoring
- Intent: expose endpoints (e.g., /health) that external tools probe regularly.
- Pitfalls: check dependencies meaningfully but cheaply; distinguish liveness vs readiness; secure endpoints; cache results to avoid overload; probe from multiple locations.

## 612. Idempotent Consumer
- Intent: duplicate message deliveries produce the same effect as one.
- How: track processed message IDs (in same transaction as state change) or make operations naturally idempotent.
- Pitfalls: dedupe store retention window; partial failures between side effect and record.

## 613. Index Table
- Intent: secondary index tables over non-key fields in NoSQL stores.
- Pitfalls: write overhead and consistency between base and index tables; denormalization choice; hot partitions in index.

## 614. Leader Election
- Intent: elect one instance to coordinate shared work.
- How: distributed lock/lease (blob lease, ZooKeeper/etcd), Raft/bully algorithms.
- Pitfalls: leader failure detection and re-election time; split brain; leader bottleneck; avoid if a single coordinator isn't needed.

## 615. Materialized View
- Intent: precomputed views over data shaped for queries.
- Pitfalls: view is eventually consistent; rebuild cost; storage; decide update triggers (events, schedule).

## 616. Messaging Bridge
- Intent: intermediary connects incompatible messaging systems (e.g., during migration).
- Pitfalls: translation fidelity, ordering, delivery guarantees across systems, extra latency.

## 617. Pipes and Filters
- Intent: decompose processing into reusable independent filters connected by pipes.
- Pitfalls: slowest filter limits throughput (scale it); reliability between steps; idempotent filters; context/state passing; added latency.

## 618. Priority Queue
- Intent: higher-priority messages processed first (single priority queue or separate queues per priority with more consumers).
- Pitfalls: low-priority starvation; cost of multiple queues; define priority clearly.

## 619. Publisher-Subscriber
- Intent: asynchronous broadcast of events to many consumers without coupling.
- Pitfalls: ordering, duplicates (idempotent subscribers), poison messages, message expiry, subscription management, not ideal when few consumers need very different info or near-real-time sync replies are needed.

## 620. Quarantine
- Intent: validate external assets (packages, images, models, data) against agreed quality/security bar before workload consumes them.
- Pitfalls: delays adoption; needs automated scanning, approval and promotion process.

## 621. Queue-Based Load Leveling
- Intent: queue between task and service absorbs bursts.
- Pitfalls: not for low-latency responses; consumers must be throttled to protect backend; queue size limits; need reply mechanism if caller expects result.

## 622. Rate Limiting
- Intent: client-side control of its own consumption to avoid hitting throttling limits (e.g., token bucket, queued sends).
- Pitfalls: coordination among distributed clients (central lease); retries must respect limits.

## 623. Retry
- Intent: handle transient faults by retrying.
- How: classify faults: rare -> retry immediately; common/busy -> retry with (exponential) backoff + jitter; non-transient -> fail.
- Pitfalls: retries amplify load (retry storms); only retry idempotent operations; cap attempts; don't retry at multiple layers; log retries; respect Retry-After; switch to circuit breaker for long-lasting faults.

## 624. Saga
- Intent: maintain consistency across services via sequence of local transactions with compensating transactions.
- Choreography: services emit/listen to events; simple but hard to track. Orchestration: central coordinator issues commands; clear but coordinator complexity.
- Pitfalls: lack of isolation (dirty reads, lost updates; use semantic locks, commutative updates, version checks, reread); compensations must be idempotent; debugging difficulty; pivot transactions and retryable steps.

## 625. Scheduler Agent Supervisor
- Intent: coordinate distributed workflow steps: scheduler drives steps, agents call remote services, supervisor monitors and recovers failed/timeout steps.
- Pitfalls: complex; state store is critical; steps must be idempotent; supervisor itself must be resilient (leader election).

## 626. Sequential Convoy
- Intent: process related messages (same session/key) in order without blocking other groups.
- How: partition by key (sessions, partition keys); one consumer per group.
- Pitfalls: throughput bounded per group; poison message blocks the group; hot keys.

## 627. Sharding
- Intent: horizontal partitions across stores.
- Strategies: Lookup (map table, flexible, extra lookup), Range (good for range queries, hotspots), Hash (even distribution, rebalancing hard).
- Pitfalls: cross-shard queries/transactions; rebalancing; referential integrity; choose immutable shard keys; avoid hotspots.

## 628. Sidecar
- Intent: deploy supporting component (logging, proxy, config, monitoring) as separate process/container beside the app sharing lifecycle.
- Pitfalls: resource overhead per instance; inter-process latency; decide when a library or daemon is better; versioning.

## 629. Static Content Hosting
- Intent: serve static assets directly from object storage/CDN.
- Pitfalls: auth for private content (use valet keys); cache headers and versioning; storage account limits; CORS.

## 630. Strangler Fig
- Intent: incrementally replace legacy functionality behind a façade that routes to old or new system.
- Pitfalls: façade must not become bottleneck/SPOF; shared data stores during transition; ensure old and new can coexist; plan to remove façade; not suitable when the legacy system is small or requests can't be intercepted.

## 631. Throttling
- Intent: provider limits resource use per tenant/user to meet SLAs under load (reject, degrade, defer, queue).
- Pitfalls: must be decided quickly; return 429 with Retry-After; combine with autoscaling (throttle while scaling); per-tenant quotas; monitoring.

## 632. Valet Key
- Intent: issue limited, time-bound token (SAS/presigned URL) granting direct client access to a specific resource, offloading data transfer from app.
- Pitfalls: scope narrowly (single object, minimum permissions, short expiry); can't easily revoke issued keys; validate uploaded content afterwards; audit usage; use HTTPS.

# Part 32 — Microservices pattern language & anti-patterns

## 633. Decompose by business capability / by subdomain
- Intent: service boundaries aligned to stable business capabilities or DDD subdomains (core, supporting, generic).
- Pitfalls: identifying capabilities requires business understanding; "god classes" spanning subdomains must be split.

## 634. Self-contained service
- Handle synchronous requests without waiting on other services (use CQRS replicas / async collaboration) for availability.

## 635. Service per team
- Each service owned by one team (Conway's law alignment); avoid shared ownership.

## 636. Strangler application / Anti-corruption layer
- Incrementally migrate monolith; ACL translates models to avoid legacy concepts leaking.

## 637. Database per service
- Each service owns private data (private tables, schema, or DB server); others access via API.
- Pitfalls: cross-service queries and transactions (need Saga, API Composition, CQRS); multiple DB technologies to operate.

## 638. Shared database (anti-pattern in most cases)
- Simple ACID transactions; but design-time and runtime coupling, schema changes block teams.

## 639. Saga (microservices)
- Sequence of local transactions with compensations; choreography or orchestration; lacks isolation.

## 640. API Composition
- Query by calling owning services and joining in memory; pitfalls: inefficient for large datasets, availability decreases with more services, no transactional consistency.

## 641. CQRS / Command-side replica
- Maintain read-optimized views via subscribed events; command-side replica keeps queryable copy of another service's data for validation.

## 642. Domain event / Event sourcing
- Publish events on state changes; event-sourced aggregates store event streams and publish reliably.

## 643. Transactional outbox
- Intent: atomically update DB and publish message.
- How: insert message into outbox table in same local transaction; relay publishes (polling publisher or transaction log tailing/CDC).
- Pitfalls: at-least-once delivery means consumers must be idempotent; ordering per aggregate; relay operation.

## 644. Polling publisher / Transaction log tailing
- Polling: simple, works with any SQL DB; adds DB load, latency.
- Log tailing (Debezium, DynamoDB Streams): low overhead, scalable; DB-specific, complex.

## 645. Consumer-driven contract test / Consumer-side contract test / Service component test
- Consumers specify expectations that provider's CI verifies (Pact); avoid end-to-end test suites as primary safety net; component tests with test doubles.

## 646. Deployment patterns
- Multiple instances per host: efficient but poor isolation.
- Instance per VM: isolation, slow start, heavy.
- Instance per container: lightweight isolation, fast; needs orchestrator.
- Serverless deployment: no infra management, pay-per-use; limits (cold start, duration, vendor lock-in).
- Service deployment platform: automated platform (Kubernetes, PaaS) providing service abstraction.

## 647. Microservice chassis / Service template
- Framework or template implementing cross-cutting concerns (config, logging, health, metrics, tracing); pitfall: one chassis per language; service mesh can replace some functions.

## 648. Externalized configuration
- Config and credentials outside code, supplied by environment/config server at startup.

## 649. Remote Procedure Invocation / Messaging / Domain-specific protocol
- RPI (REST/gRPC): simple, request/response; reduced availability due to temporal coupling.
- Messaging: loose coupling, buffering, async; broker complexity, eventual consistency.
- Domain-specific: SMTP, streaming protocols when domain demands.

## 650. Idempotent consumer
- Record processed message IDs; required because brokers deliver at least once.

## 651. API gateway / Backend for front-end
- Single entry for clients performing routing, composition, protocol translation, auth; BFF variant per client type; pitfalls: gateway as bottleneck, must be developed/deployed by owning teams.

## 652. Service discovery (client-side, server-side, registry, self/3rd-party registration)
- Client-side: client queries registry and load balances (fewer hops; language-specific client logic).
- Server-side: router/LB queries registry (simpler clients; another component; e.g., Kubernetes Services).
- Registry must be highly available; self-registration couples services to registry; 3rd-party registrar (platform) decouples.

## 653. Circuit breaker (microservices)
- Proxy that trips when failures exceed threshold; fail fast with fallbacks; prevents cascading failures and thread exhaustion.

## 654. Access token
- API gateway authenticates and passes token (e.g., JWT) carrying identity/claims to services; services verify token, not session.

## 655. Observability patterns
- Log aggregation (centralized, searchable logs), application metrics (RED/USE), audit logging, distributed tracing (correlation/trace IDs propagated), exception tracking (deduped, alerting), health check API, log deployments and changes (correlate incidents with changes).

## 656. UI composition
- Server-side page fragment composition (SSI/ESI) or client-side composition (micro-frontends) so each team owns its UI slice.

## 657. Anti-pattern: Data-driven migration
- Migrating code and data simultaneously when splitting a monolith; each granularity change forces another data migration.
- Fix: migrate functionality first, stabilize service granularity, then migrate data; shared data as a temporary step.

## 658. Anti-pattern: Timeout
- Long timeouts make failures slow; short ones cancel successful operations.
- Fix: circuit breaker with health monitoring (heartbeats, synthetic transactions, real-time traffic).

## 659. Anti-pattern: "I was taught to share"
- Excessive shared code creates dependency hell.
- Fix: share little; prefer versioned, context-specific libraries over catch-all "common" library; consider replicating stable code or consolidating services.

## 660. Anti-pattern: Reach-in reporting
- Reporting directly reading service databases couples to schemas.
- Fix: services push reportable events asynchronously to a reporting service that owns its database.

## 661. Pitfall: Grains of sand
- Services too fine-grained (service = class); excessive network calls, distributed transactions.
- Fix: assess scope/cohesion, transactional needs, choreography; start coarse, split later.

## 662. Pitfall: Developer without a cause / Jump on the bandwagon
- Decisions not tied to business drivers; adopting microservices because trendy.
- Fix: identify business drivers and architecture characteristics; consider alternatives (service-based, modular monolith).

## 663. Pitfall: Static contract
- Unversioned contracts break consumers.
- Fix: version contracts from day one (header-based or schema-based); deprecation policy.

## 664. Pitfall: Are we there yet
- Ignoring remote call latency; long tail unmeasured.
- Fix: measure average and p95-p99.5 latency under production-like load; choose faster protocols where needed.

## 665. Pitfall: Give it a REST
- Using REST for everything.
- Fix: use messaging for fire-and-forget, broadcast, and transactional multi-service requests.

## 666. Anti-pattern: Distributed monolith [general]
- Services must deploy together due to synchronous chains and shared DB; worst of both worlds.
- Fix: async communication, database per service, consumer-driven contracts, independent deployability as a test.

# Part 33 — Twelve-factor app

## 667. I. Codebase
- One codebase per app in version control, many deploys (dev, staging, prod).
- Multiple codebases = distributed system; shared code goes into libraries via dependency manager; multiple apps sharing one repo violates the factor.

## 668. II. Dependencies
- Explicitly declare (manifest) and isolate (virtualenv, bundler, lockfiles) all dependencies; never rely on implicit system-wide packages or tools (curl, ImageMagick) - vendor them.

## 669. III. Config
- Store config (DB URLs, credentials, per-deploy values) in environment variables; strict separation of config from code.
- Test: could the codebase be open-sourced without leaking credentials? Avoid grouping into named environments ("staging", "prod") - use granular independent env vars.

## 670. IV. Backing services
- Treat DBs, queues, SMTP, caches as attached resources addressed by URL/credentials in config; swap local for third-party without code change.

## 671. V. Build, release, run
- Strictly separate stages: build (compile artifacts), release (build + config, immutable, unique ID), run (execute). No code changes at runtime; rollbacks select prior release.

## 672. VI. Processes
- Execute as stateless, share-nothing processes; persist state in backing services; no sticky sessions; memory/filesystem only as brief single-transaction cache.

## 673. VII. Port binding
- App is self-contained and exports HTTP (or other protocol) by binding to a port; no runtime injection into an external web server; one app can be another's backing service.

## 674. VIII. Concurrency
- Scale out via the process model; assign workload types to process types (web, worker); rely on OS process manager / platform, never daemonize or write PID files.

## 675. IX. Disposability
- Fast startup, graceful shutdown on SIGTERM (stop accepting, finish in-flight, return jobs to queue); robust against sudden death; jobs idempotent/reentrant.

## 676. X. Dev/prod parity
- Minimize time gap (deploy hours after writing), personnel gap (devs deploy), tools gap (same backing service types and versions); avoid lightweight local substitutes (SQLite vs Postgres).

## 677. XI. Logs
- Treat logs as event streams written unbuffered to stdout; the execution environment routes to aggregation/analysis; app never manages log files.

## 678. XII. Admin processes
- Run admin/maintenance tasks (migrations, consoles, one-off scripts) as one-off processes in identical environment, same codebase and config as release.

# Part 34 — Messaging / Enterprise Integration Patterns

## 679. Integration styles: File Transfer, Shared Database, Remote Procedure Invocation, Messaging
- File transfer: simple, decoupled, but latency and stale data, format agreements.
- Shared DB: consistent, immediate; strong schema coupling and contention.
- RPI: synchronous, encapsulated; temporal coupling, cascading failures.
- Messaging: async, reliable, decoupled; complexity, eventual consistency, debugging harder. Prefer messaging for loose coupling.

## 680. Message Channel / Message / Message Endpoint
- Channels are logical addresses; messages = header + body; endpoints encapsulate app-to-messaging code.

## 681. Pipes and Filters / Message Router / Message Translator
- Compose processing from filters on channels; router chooses destination without changing message; translator converts formats between systems.

## 682. Point-to-Point Channel vs Publish-Subscribe Channel
- P2P: exactly one consumer gets each message (work distribution, commands).
- Pub-sub: every subscriber gets a copy (events).

## 683. Datatype Channel
- One channel per message type so receivers know how to interpret.

## 684. Invalid Message Channel / Dead Letter Channel
- Invalid: receiver can't process (malformed) -> move aside for inspection.
- Dead letter: messaging system can't deliver (expired, too many retries).
- Rule: always monitor and alert on these channels; provide replay tooling.

## 685. Guaranteed Delivery
- Persist messages to disk so they survive broker crashes; costs throughput and storage.

## 686. Channel Adapter / Messaging Bridge / Message Bus
- Adapter connects non-messaging apps; bridge connects messaging systems; bus = canonical data model + shared command set + channel infrastructure for plug-and-play apps.

## 687. Command Message / Document Message / Event Message
- Command: invoke a procedure (one receiver). Document: transfer data. Event: notification of something that happened (many receivers, minimal data or full state).

## 688. Request-Reply / Return Address / Correlation Identifier
- Request includes Return Address (reply channel) and correlation ID so requestor matches async replies.

## 689. Message Sequence / Message Expiration / Format Indicator
- Sequence: split large data with sequence id, position, end indicator.
- Expiration: TTL so stale messages are discarded/dead-lettered.
- Format indicator: version field/schema ID to evolve formats.

## 690. Content-Based Router / Message Filter / Dynamic Router / Recipient List
- CBR: route on message content (centralized knowledge of destinations).
- Filter: drop uninteresting messages.
- Dynamic router: destinations register rules at runtime via control channel.
- Recipient list: compute list of recipients and send copies.

## 691. Splitter / Aggregator / Resequencer
- Splitter breaks composite message into parts.
- Aggregator collects related messages (correlation ID) until completeness condition (count, timeout, external event) then publishes one; pitfall: state and timeouts.
- Resequencer buffers out-of-order messages and emits in order; bounded buffer to avoid unbounded wait.

## 692. Composed Message Processor / Scatter-Gather
- CMP: split, route each part, aggregate.
- Scatter-gather: broadcast to multiple recipients (quotes), aggregate replies with timeout.

## 693. Routing Slip / Process Manager / Message Broker
- Routing slip: sequence of steps attached to message (static itinerary).
- Process manager: central component maintains state and decides next step (complex, conditional flows; like saga orchestrator).
- Message broker: hub-and-spoke central routing; decouples but may become bottleneck.

## 694. Envelope Wrapper / Content Enricher / Content Filter / Claim Check / Normalizer / Canonical Data Model
- Envelope: wrap payload with required headers/security.
- Enricher: add missing data from external source.
- Content filter: remove unneeded fields (also security).
- Claim check: store payload, pass reference.
- Normalizer: route differing formats to translators into one common format.
- Canonical data model: shared format reduces N^2 translators to 2N; pitfall: bloated "enterprise model" coupling.

## 695. Messaging Gateway / Messaging Mapper / Transactional Client / Service Activator
- Gateway hides messaging API behind domain interface; mapper converts domain objects to messages; transactional client groups send/receive with DB work; service activator lets service be invoked by messages or synchronously.

## 696. Polling Consumer / Event-Driven Consumer / Competing Consumers / Message Dispatcher / Selective Consumer
- Polling: consumer controls rate (throttling); event-driven: callback on arrival; competing: parallel consumers for throughput; dispatcher: one receiver distributes to performers; selective: filter by criteria (selectors).

## 697. Durable Subscriber / Idempotent Receiver
- Durable: broker keeps messages for disconnected subscribers.
- Idempotent receiver: dedupe by message ID or make operations idempotent (at-least-once is the norm).

## 698. Control Bus / Detour / Wire Tap / Message History / Message Store / Smart Proxy / Test Message / Channel Purger
- Control bus: separate channel for management (config, heartbeat, stats).
- Detour: switchable route through validation/debug steps.
- Wire tap: copy messages to secondary channel for monitoring.
- Message history: list of components traversed.
- Message store: store copies for reporting/analysis.
- Smart proxy: intercepts request-reply to track replies.
- Test message: inject synthetic messages to verify health.
- Channel purger: clear leftover messages for tests or recovery.

# Part 35 — Serverless

## 699. Event-driven data processing (The New Stack)
- Event (object upload, DB change) triggers function (e.g., S3 -> Lambda to compress image).
- Use for async, stateless, ephemeral work; hybrid add-ons to existing systems.
- Pitfalls: stateful workflows need external state or orchestration; recursion loops (function writes to bucket that triggers itself).

## 700. Serverless web application
- Static assets in object storage/CDN; API Gateway -> functions -> managed DB (DynamoDB) for dynamic per-user content.
- Pitfalls: cold starts on latency-sensitive endpoints; many moving managed parts to configure.

## 701. Mobile/IoT backend
- Managed authentication (Cognito-like) + functions + DB; authorize per user/device type.
- Pitfalls: auth model must fit user categories (employees, partners, customers, machines).

## 702. Application ecosystems / third-party integration
- Functions glue managed services and external APIs (voice assistant -> function -> chat API).
- Pitfalls: third-party API dependency and rate limits; polling for responses.

## 703. Event workflows (state machines)
- Step Functions-style orchestration for multi-step processes with branches, retries, waits.
- Pitfalls: cost per state transition; throttling limits; regional availability; purely async.

## 704. Simple Web Service
- API Gateway -> Lambda -> DynamoDB. Pitfall: non-elastic DBs (RDS) bottleneck under function concurrency (connection exhaustion; use proxies).

## 705. Scalable Webhook
- API Gateway -> SQS -> throttled Lambda; absorbs bursts and protects downstream. Pitfall: processing delay under heavy load.

## 706. Gatekeeper (Lambda authorizer)
- Authorizer function validates token and returns IAM policy; cached by gateway for TTL. Pitfall: cached policy delays revocation.

## 707. Internal API / Internal Handoff
- Internal API: synchronous function-to-function invocation (caller waits and pays).
- Internal Handoff: async invocation with ack; at-least-once -> idempotent handlers + DLQ + monitoring.

## 708. Aggregator
- One function calls multiple services and merges results; latency = slowest dependency; pay for waiting.

## 709. Notifier
- Standalone pub/sub topic as a service boundary; subscribers self-register; decouples publishers.

## 710. FIFOer
- Ordered processing from FIFO queue; prior workaround (scheduled concurrency-1 self-invoking function) superseded by native FIFO queue triggers.

## 711. Continuous stream ("They Say I'm A Streamer")
- API Gateway proxy -> Kinesis (sharded) -> Firehose -> S3/warehouse; cheaper than pub/sub at high volume.

## 712. Strangler (serverless)
- API Gateway routes legacy endpoints by default and new routes to functions incrementally.

## 713. State Machine / Router
- State machine: orchestration with retries, waits, rollback, encapsulated inside one service; can't return synchronously to caller.
- Router: function dispatches to task functions by type; cheaper than state machines but less state management; need DLQs.

## 714. Robust API
- Gateway routes by method/path across multiple services sharing data sources; flexible but complex.

## 715. Frugal Consumer
- Services post directly to a queue drained by a throttled function; no gateway cost.

## 716. Read-Heavy Reporting Engine
- Cache (ElastiCache) in front of RDB to cut reads and connections; manage TTL/invalidation; only open DB connection on miss.

## 717. Fan-Out / Fan-In
- Split large job across async worker invocations; results gathered in shared store; works around function timeouts; needs DLQs and explicit aggregation/completion tracking.

## 718. Eventually Consistent (stream replication)
- DB stream triggers function to replicate into relational store; bad record blocks in-order batch retries (DLQ, bisect); use last_updated to avoid overwriting newer data; throttle to protect target DB.

## 719. Distributed Trigger
- Event sources publish to single-purpose topic owned by one service; consumers subscribe independently.

## 720. Circuit Breaker (serverless)
- Store breaker state externally (DynamoDB/cache) since functions are stateless; fail fast on failing third-party APIs; tune backoff.

## 721. Serverless cross-cutting rules [general]
- Keep functions small, single-purpose, stateless; set concurrency limits to protect downstream; DLQ/failure destinations for all async invocations; idempotency everywhere; watch timeouts (function < gateway < queue visibility timeout); beware cold starts and vendor lock-in.

# Part 36 — Containers & Kubernetes (k8spatterns categories; site blocked, [general])

## 722. Foundational: Predictable Demands
- Declare resource requests/limits and runtime dependencies (PVCs, ConfigMaps) so scheduler can place pods; set QoS classes (Guaranteed/Burstable/BestEffort) deliberately; use ResourceQuotas/LimitRanges.

## 723. Foundational: Declarative Deployment
- Use Deployments for rolling updates (maxSurge/maxUnavailable), recreate, blue-green, canary; requires readiness probes and backward-compatible changes.

## 724. Foundational: Health Probe
- Liveness (restart when stuck), readiness (remove from service when not ready), startup probes for slow starts; pitfalls: liveness checking dependencies causes cascading restarts.

## 725. Foundational: Managed Lifecycle
- Handle SIGTERM gracefully within terminationGracePeriod; use postStart/preStop hooks; init containers for ordered setup.

## 726. Foundational: Automated Placement
- Node selectors, affinity/anti-affinity, taints/tolerations, topology spread to place pods for HA and resource fit.

## 727. Behavioral: Batch Job / Periodic Job (CronJob)
- Jobs for run-to-completion tasks with completions/parallelism and backoff; CronJobs with concurrencyPolicy; idempotent jobs.

## 728. Behavioral: Daemon Service
- DaemonSet runs one pod per node for infrastructure agents (logs, monitoring, networking).

## 729. Behavioral: Singleton Service
- Ensure only one active instance: out-of-application (StatefulSet replicas=1) or in-application leader election (leases); PodDisruptionBudget.

## 730. Behavioral: Stateless Service / Stateful Service
- Stateless: ReplicaSet/Deployment, horizontally scalable.
- Stateful: StatefulSet gives stable network identity, ordered startup, per-pod persistent volumes; still need application-level replication.

## 731. Behavioral: Service Discovery
- Kubernetes Services (ClusterIP, headless), DNS, NodePort/LoadBalancer/Ingress for external access.

## 732. Behavioral: Self Awareness
- Downward API exposes pod metadata (name, IP, resource limits) to the app via env/volumes.

## 733. Structural: Init Container
- Run setup tasks (migrations, permissions, waiting for dependencies) before app containers; separate lifecycle concerns.

## 734. Structural: Sidecar
- Helper container extends main container (log shipping, proxy, sync); shares network and volumes.

## 735. Structural: Adapter
- Sidecar that normalizes heterogeneous outputs (e.g., metrics to Prometheus format) to a common interface.

## 736. Structural: Ambassador
- Sidecar proxy that hides external service access complexity (sharding, retries, auth) from main container.

## 737. Configuration: EnvVar Configuration / Configuration Resource / Immutable Configuration / Configuration Template
- Env vars for small config; ConfigMaps/Secrets for larger; immutable config images/ConfigMaps for versioned, reproducible configs; templates rendered at init for environment-specific files. Rotate pods on config change.

## 738. Security patterns: Process Containment, Network Segmentation, Secure Configuration, Access Control
- Run as non-root, drop capabilities, read-only root FS, seccomp; NetworkPolicies default-deny; store secrets encrypted (external secret stores); RBAC least privilege for service accounts.

## 739. Advanced: Controller / Operator
- Controller reconciles desired vs actual state in a loop; Operator encodes domain operational knowledge with CRDs (backup, failover, upgrade). Pitfalls: complexity, idempotent reconcile, avoid hot loops.

## 740. Advanced: Elastic Scale
- HPA (CPU/custom metrics), VPA, cluster autoscaler; set sensible min/max; scale-down stabilization.

## 741. Advanced: Image Builder
- Build images in-cluster (Buildpacks, Kaniko, OpenShift builds) reproducibly.

## 742. Container anti-patterns [general; l0rd containerspatterns page body not retrievable]
- Don't store data in containers (use volumes); don't ship app in two pieces/install at runtime; avoid huge images (multi-stage builds, minimal bases); one process concern per container; don't use "latest" tag in production; don't run as root; don't hardcode IPs; don't put secrets/credentials in images; don't rely on image-based config per environment; build once, promote same image across environments.

# Part 37 — Streaming, data & ML

## 743. Preprocessing
- Filter, project, reshape, split/combine attributes, transform values to produce clean derived streams before analytics.

## 744. Alerts and thresholds
- Detect simple threshold violations or complex conditions (rate of increase over window) and emit alerts; avoid alert storms with dedupe/hysteresis.

## 745. Simple counting and windowed counting
- Incremental aggregates (count, min, max, percentiles via sketches) without storing all data; windows: time vs length, sliding vs tumbling/batch.
- Pitfalls: late/out-of-order events (watermarks), window state memory.

## 746. Joining event streams
- Join multiple streams by condition within a window (e.g., sensor proximity); bounded join windows required.

## 747. Data correlation, missing events, erroneous data
- Correlate events across streams/rates, detect absence (no response within timeout), detect faulty sensor readings with redundancy.

## 748. Interacting with databases
- Enrich stream events with historical/reference data (customer profile, blacklists); cache lookups to avoid per-event DB latency.

## 749. Detecting temporal event sequence patterns
- Regex-like CEP over ordered events (small transaction then large one -> fraud).

## 750. Tracking
- Follow entities over time/space; geofences, route deviations, logistics bottlenecks.

## 751. Detecting trends
- Rise, fall, turn, outliers, complex shapes in time series; drives trading, autoscaling, predictive maintenance.

## 752. Same query in batch and realtime (Lambda architecture)
- Realtime pipeline fills gap until batch catches up; pitfall: maintaining two codebases (Kappa architecture: single streaming path with replay).

## 753. Detect and switch to detailed analysis
- Cheap realtime filter flags anomalies, triggers expensive deep analysis on history only for flagged cases.

## 754. Using a model
- Train offline, score in stream (export via PMML/ONNX); monitor drift and retrain.

## 755. Online control
- Continuous assess-predict-act loops (autopilot, robotics); strict latency and safety requirements.

## 756. Distributed ML: data ingestion patterns
- Batching (process dataset in chunks that fit memory), sharding (split dataset across workers), caching (cache preprocessed data for multiple epochs). Pitfalls: shard skew, cache invalidation when data changes.

## 757. Distributed ML: training patterns
- Parameter server (workers push gradients, servers aggregate; bottleneck on servers), collective communication / allreduce (ring allreduce, no central server; sensitive to stragglers), elastic & fault-tolerant training (checkpointing, dynamic worker membership).

## 758. Distributed ML: model serving patterns
- Replicated services (stateless replicas behind LB), sharded services (split large requests/models across shards), event-driven processing (autoscale on demand, queue-backed inference).

## 759. Distributed ML: workflow patterns
- Fan-in/fan-out pipelines (train multiple models, ensemble), synchronous vs asynchronous steps, step memoization (skip unchanged steps via caching). Orchestrators: Kubeflow, Argo Workflows.

## 760. Distributed ML: operation patterns
- Scheduling (gang scheduling so all workers start together; priority/fair share), metadata tracking (lineage, experiment tracking), monitoring of failures and resource usage.

# Part 38 — Database design & SQL anti-patterns

## 761. Common lookup table (MUCK / One True Lookup Table)
- Problem: one generic table for all code types (statuses, locations, discount types) prevents proper FKs and type-specific constraints, forces string types, causes locking/perf issues.
- Fix: one table per logical domain with proper types and FKs.

## 762. Check constraint vs lookup table
- Use check constraint for short, stable value lists; use a referenced lookup table if values change, exceed ~15-20 items, or are reused across several tables. Don't omit constraints.

## 763. Entity-Attribute-Value (EAV)
- Problem: attributes stored as name/value rows; no typing, no constraints, no FKs, pivot-heavy queries, poor performance.
- Fix: gather requirements and model typed columns; if truly dynamic, consider JSON columns with validation or separate subtype tables.

## 764. Application encroachment on database design
- Problem: integrity only in app code, ad-hoc table/column additions; multiple apps enforce inconsistently; DB outlives apps.
- Fix: declare constraints (PK, FK, UNIQUE, CHECK, NOT NULL) in DB; triggers/procs only when declarative can't express rule; design from business rules.

## 765. Data values as data elements (attribute splitting)
- Problem: repeating columns per period (Jan_sales, Feb_sales) or tables per value (Sales2023); schema changes for new periods; awkward queries.
- Fix: one row per entity per period; separate entity table; UNPIVOT legacy wide tables.

## 766. Multi-valued attribute (jaywalking)
- Comma-separated lists in a column break 1NF, indexing, FK integrity and length limits; use intersection table.

## 767. Recursive dependency (naive trees)
- Adjacency-list parent_id makes deep traversal hard; use recursive CTEs, closure table, nested sets, or path enumeration by query needs.

## 768. Missing primary key / generic "id" primary key
- Every table needs a PK; avoid meaningless "id" everywhere when natural or compound keys fit (or at least name keys descriptively, e.g., order_id) and prevent duplicate rows via unique constraints.

## 769. Missing foreign keys
- Without FKs, orphaned rows accumulate; declare FKs (and index FK columns).

## 770. Metadata tribbles
- Cloning tables/columns per year/customer (Bugs_2023, tag1..tag3); use partitioning or normalized rows.

## 771. Imprecise data types
- FLOAT/REAL for money or exact values causes rounding errors; use NUMERIC/DECIMAL.

## 772. Values in definition (ENUM)
- Enum lists in column definitions need DDL to change and hide values; use lookup tables.

## 773. Files are not SQL data types / phantom files
- Storing only file paths loses transactional integrity, backups, access control; or BLOBs bloat DB; choose deliberately and keep references consistent.

## 774. Too many / too few indexes; index attribute order
- Index for actual queries (MENTOR: measure, explain, nominate, test, optimize, rebuild); excess indexes slow writes; composite index column order must match query predicates (leftmost prefix, equality before range).

## 775. SELECT *
- Fetches unneeded columns, breaks covering indexes, fragile on schema change; list columns explicitly.

## 776. NULL usage / NOT NULL usage
- NULL is not a value: comparisons yield unknown; use IS NULL, COALESCE; don't use sentinel values; add NOT NULL where data is required.

## 777. String concatenation in queries
- Concatenation with NULL yields NULL; dynamic SQL via concatenation invites injection - use bound parameters.

## 778. GROUP BY ambiguity
- Selecting non-aggregated columns not in GROUP BY gives ambiguous results; follow single-value rule.

## 779. ORDER BY RAND()
- Full scan + sort; pick random rows via random offset, key ranges, or app-side selection.

## 780. Pattern matching (LIKE '%x%', regex)
- Leading wildcards can't use B-tree index; use full-text search.

## 781. Spaghetti query
- One giant query solving everything (often accidental Cartesian products); split into simpler queries or CTEs.

## 782. Too many JOINs / unnecessary DISTINCT / DISTINCT masking join duplicates
- Excess joins hurt performance; DISTINCT used to hide incorrect join multiplicity signals a bug; fix the join or use EXISTS.

## 783. Implicit columns in INSERT
- INSERT without column list breaks when schema changes; always name columns.

## 784. HAVING vs WHERE
- Filter rows in WHERE before aggregation; HAVING only for aggregate conditions.

## 785. Nested subqueries / OR usage / UNION usage
- Deep nesting hurts readability and plans (use joins/CTEs); OR across columns may defeat indexes (use UNION ALL or IN); prefer UNION ALL when duplicates impossible (avoids sort).

## 786. Readable passwords
- Never store plaintext or reversibly encrypted passwords; salted slow hashes (bcrypt/scrypt/Argon2).

# Part 39 — Security by design principles

## 787. Minimize attack surface
- Each feature adds risk; remove or restrict features, endpoints, ports, admin interfaces, and unauthenticated functionality.

## 788. Establish secure defaults
- Ship with the most secure settings on (password policy, MFA, TLS); allow loosening only where policy permits.

## 789. Least privilege
- Grant accounts, services, and processes only the permissions needed (specific tables, read-only where possible), for the minimal time.

## 790. Defense in depth
- Layer independent controls (network restrictions + authorization + logging + input validation) so one failure doesn't compromise the system.

## 791. Fail securely
- Errors default to deny; never grant privileges before checks that can throw; exceptions must not leak internals.

## 792. Don't trust services
- Validate data from partners, third-party APIs, and upstream services as untrusted input (range checks, schema).

## 793. Separation of duties
- No single role controls a whole sensitive process; admins shouldn't act as end users (e.g., can't purchase on behalf of others).

## 794. Avoid security by obscurity
- Secrecy of design is not a control; rely on strong mechanisms (crypto, authN/Z, audit) that hold even if design is public.

## 795. Keep security simple
- Simple designs have fewer flaws; avoid elaborate architectures where simpler concurrency/security constructs suffice.

## 796. Fix security issues correctly
- Find root cause, add regression test, check shared components across apps for the same flaw.

## 797. Treat all input as untrusted; validate on server (Fowler)
- Validate every input source (forms, JSON, headers, cookies, URL params) server-side; prefer allowlists (type, length, range, format); reject rather than sanitize; validate before business logic; log rejections; don't echo raw input in errors.

## 798. Contextual output encoding
- Encode at render time for the target context (HTML, attribute, JS, URL, CSS); use framework auto-escaping; avoid raw HTML APIs (innerHTML, unescaped template helpers); minimize nested contexts.

## 799. Parameter binding
- Never build SQL/NoSQL/LDAP/OS commands by string concatenation; use bound parameters everywhere including ORMs and stored procs; check NoSQL unsafe operators.

## 800. HTTPS everywhere + HSTS
- Serve all content over TLS with current config; redirect HTTP->HTTPS; HSTS (after verifying all resources load via HTTPS); Secure cookies; no sensitive data in URLs; disable caching of sensitive responses; scan config periodically.

## 801. Password storage
- Slow adaptive hashes (bcrypt, scrypt, Argon2), unique per-user random salt (>=128 bits), configurable work factor with stored algorithm metadata for upgrades; never MD5/SHA for passwords; allow long passwords (min 12, allow >=100), permit paste and password managers.

## 802. Authentication
- Use mature frameworks; MFA (TOTP/hardware > SMS) for sensitive apps; reauthenticate for sensitive actions; generic error messages to prevent account enumeration (also on registration/reset); layered brute-force protection (short lockouts, CAPTCHA, escalation); no default or hard-coded credentials.

## 803. Session management
- Framework sessions; IDs >=128 bits from CSPRNG; server-side session data (no secrets/PII in cookies; sign/encrypt if necessary); IDs only in cookies (never URLs/logs); cookie flags Secure, HttpOnly, narrow Domain/Path (SameSite [general]); regenerate session on login and privilege change (fixation); reject unknown IDs; idle timeouts by risk; logout invalidates; terminate sessions on password change; let users see/revoke sessions.

## 804. Authorization
- Enforce on server (hidden UI isn't control); never accept roles/permissions from client; deny by default; check both action permission and resource ownership (prevents IDOR); check permissions not role names; RBAC for stable domain roles, ABAC for dynamic/attribute-based rules; centralize authorization logic; Cache-Control: private, no-store on protected responses.

# Part 40 — Reactive principles & patterns (Reactive Design Patterns)

## 805. Reactive Manifesto traits [general]
- Responsive (timely responses), resilient (stay responsive under failure via replication, containment, isolation, delegation), elastic (scale with load, no contention points), message-driven (async message passing, location transparency, back-pressure).

## 806. Simple Component
- Each component does one thing fully (single responsibility); simplifies supervision and replacement.

## 807. Error Kernel
- Keep critical state and functions in a small, robust core near the root of the supervision hierarchy; push risky operations to leaf (disposable) components.

## 808. Let-it-crash
- Don't defensively handle every failure inside a component; let it fail and have its supervisor restart it in a clean state; requires isolation and supervision.

## 809. Circuit Breaker (reactive)
- Protect services from overload by failing fast when downstream is unhealthy; part of flow control and fault containment.

## 810. Active-Passive replication
- One active replica serves; others take over on failure; simple consistency, failover gap.

## 811. Multiple-Master replication: consensus-based, conflict detection & resolution, CRDTs
- Consensus: strong consistency at cost of latency/availability under partitions.
- Conflict detection/resolution: accept writes everywhere and reconcile later (version vectors, app merges).
- CRDTs: data types whose concurrent updates merge deterministically (counters, sets) - convergence without coordination; limited operation sets.

## 812. Active-Active replication
- All replicas process every request; respond with first result; masks failures with no failover time; costly and requires deterministic processing.

## 813. Resource Encapsulation / Resource Loan / Resource Pool
- Encapsulation: a component owns and manages its resource's lifecycle.
- Loan: grant temporary exclusive use while owner retains responsibility.
- Pool: hide elastic pool of resources behind one component that dispatches work.

## 814. Complex Command
- Send behavior (a batch job/command) to where the data/resource lives instead of moving data.

## 815. Managed Blocking
- Isolate unavoidable blocking calls on dedicated, bounded thread pools so they don't starve the main event loop.

## 816. Request-Response / Self-Contained Message
- Include return address and correlation in requests; messages carry all information needed to process them (no shared context).

## 817. Ask pattern
- Spawn a temporary child/promise to await a reply with timeout, turning a message exchange into a future.

## 818. Forward Flow
- Route messages directly to their final destination rather than through each intermediary returning back (reduces hops).

## 819. Aggregator (reactive)
- Collect multiple responses into one result with timeouts for missing responses.

## 820. Saga (reactive)
- Long-running distributed transaction split into steps with compensations.

## 821. Business Handshake (reliable delivery)
- Include business-level identifiers and acknowledgements so that resends are idempotent and delivery is confirmed end to end (at-least-once + idempotency = effectively once).

## 822. Pull
- Consumer requests work as capacity allows (demand signaling), preventing overload.

## 823. Managed Queue
- Bounded queue with monitoring; queue length signals load and drives rejection or scaling.

## 824. Drop
- Under overload, drop (or degrade) requests intentionally rather than collapsing; prefer dropping early and cheaply.

## 825. Throttling (reactive)
- Limit request rate to what downstream can sustain (token bucket), coordinated with pull/demand.

## 826. Domain Object
- Separate business domain logic from messaging/persistence concerns; domain object is a pure model.

## 827. Sharding (reactive)
- Partition state into many shards distributed across nodes for elastic scaling of stateful components.

## 828. Event Sourcing / Event Stream
- Persist state changes as event log; publish event stream for other components to consume (CQRS projections), decoupling reads from writes.
