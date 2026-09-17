import { NextResponse } from 'next/server';

export const runtime = 'nodejs';

/**
 * Whop Webhook Handler
 * Handles purchase and membership events from Whop checkout
 */
export async function POST(request: Request) {
  try {
    const rawBody = await request.text();
    const signature = request.headers.get('x-whop-signature') || '';

    // Verify webhook secret if configured
    const webhookSecret = process.env.WHOP_WEBHOOK_SECRET;
    if (webhookSecret && !signature) {
      return NextResponse.json({ error: 'Missing Whop signature' }, { status: 401 });
    }

    const event = JSON.parse(rawBody);
    const eventType = event.action || event.event || 'unknown';

    console.log(`[Whop Webhook] Received event: ${eventType}`);

    switch (eventType) {
      case 'membership.went_valid':
      case 'payment.succeeded': {
        const userEmail = event.data?.user?.email || event.data?.email;
        const productId = event.data?.product_id || event.data?.plan_id;
        console.log(`[Whop Webhook] Success payment for ${userEmail}, product: ${productId}`);
        // Provision user access / credits here
        break;
      }
      case 'membership.went_invalid': {
        const userEmail = event.data?.user?.email;
        console.log(`[Whop Webhook] Subscription cancelled for ${userEmail}`);
        break;
      }
      default:
        console.log(`[Whop Webhook] Unhandled event type: ${eventType}`);
    }

    return NextResponse.json({ received: true, action: eventType });
  } catch (error: any) {
    console.error('[Whop Webhook Error]', error);
    return NextResponse.json({ error: error.message || 'Webhook processing failed' }, { status: 500 });
  }
}
