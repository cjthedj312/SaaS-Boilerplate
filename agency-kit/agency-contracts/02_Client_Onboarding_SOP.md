# Standard Operating Procedure (SOP): 48-Hour Client Onboarding

**Goal:** Take a new client from initial payment to fully operational missed-call automation in under 48 hours with zero manual phone calls.

---

### Step 1: Automated Payment & Intake (Hour 0)
1. Client completes checkout via Whop / Stripe link (\$97–\$200 setup).
2. Webhook triggers automated email with the 3-minute intake form:
   - Business Name & primary service area
   - Primary forwarding cell phone number
   - Desired Calendly / booking URL
   - Business hours (for out-of-hours auto-responses)

### Step 2: Line & Workflow Provisioning (Hours 1–12)
1. Provision local area code number in Twilio (e.g., 719 for Colorado Springs).
2. Configure webhook URL pointing to the n8n / Next.js missed-call handler.
3. Set call forwarding rule: Incoming call rings client's mobile for 20 seconds. If unanswered, trigger `no-answer` webhook.

### Step 3: SMS Copy Customization (Hours 12–24)
1. Insert client's business name and booking link into the SMS template:
   > *"Hi, this is [Client Business Name]! Sorry we missed your call—we're currently on a job. Tap here to lock in your appointment or quote: [Link]"*

### Step 4: Smoke Test & Handoff (Hours 24–48)
1. Make 1 test call to the client's new number from a test phone.
2. Let it ring out; confirm test SMS is delivered within 10 seconds.
3. Send client the "You're Live" confirmation email with their dashboard login.
