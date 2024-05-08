from .models import Costumer, Order
from django.http import JsonResponse


def total_order_sum_per_user(request):
    # barcha userlarni olamiz
    all_users = Costumer.objects.all()

    user_order_sum = {}

    for user in all_users:
        user_orders = Order.objects.filter(costumer_user=user)

        total_sum = 0

        for order in user_orders:
            total_sum += order.order_price

        user_order_sum[user.name] = total_sum

    return JsonResponse(user_order_sum)
