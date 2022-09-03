from django.apps import AppConfig


class CheckoutConfig(AppConfig):
    """
    Checkout App configuration
    """
    name = 'checkout'

    def ready(self):
        import checkout.signals
