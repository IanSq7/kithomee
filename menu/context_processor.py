def total_carrito(request):
    total = 0
    if request.user.is_authenticated:
        if 'carrito' in request.session:
            for key, value in request.session["carrito"].items():
                total += (int(value["precio"])*value["cantidad"])
    return {"total_carrito": total}