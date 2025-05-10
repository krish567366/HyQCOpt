import stripe
from fastapi import APIRouter, Depends
from ..middleware.auth import get_current_user

router = APIRouter()
stripe.api_key = os.getenv('STRIPE_SECRET_KEY')

@router.post("/create-subscription")
async def create_subscription(price_id: str, user=Depends(get_current_user)):
    session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[{
            'price': price_id,
            'quantity': 1,
        }],
        mode='subscription',
        success_url=f"{os.getenv('FRONTEND_URL')}/success?session_id={{CHECKOUT_SESSION_ID}}",
        cancel_url=f"{os.getenv('FRONTEND_URL')}/cancel",
        metadata={'user_id': user['id']}
    )
    return {'session_id': session.id}

@router.post("/stripe-webhook")
async def webhook(request: Request):
    payload = await request.body()
    sig_header = request.headers.get('stripe-signature')
    event = stripe.Webhook.construct_event(
        payload, sig_header, os.getenv('STRIPE_WEBHOOK_SECRET')
    )
    
    if event['type'] == 'checkout.session.completed':
        handle_payment_success(event['data']['object'])
    
    return {'status': 'received'}

def handle_payment_success(session):
    user_id = session['metadata']['user_id']
    # Update user tier in database