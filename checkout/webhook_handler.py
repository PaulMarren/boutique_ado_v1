from django.http import HttpResponse


class StripeWH_Handler:
    """Handle Stripe webhooks"""

    def __init__(self, request):
        self.request = request

    def handle_event(self, order):
        """Handle a generic/unknown/unexpected webhook"""
        return HttpResponse(
            content=f"Webhook received: {self.request['type']}",
            status=200,
        )