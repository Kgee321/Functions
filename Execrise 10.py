def calc_gst(net_price):
    result = net_price * 1.15
    return f"With GST added on, {net_price} is now ${result:.2f} (2dp)"


number = float(input("Enter number: "))
print(calc_gst(number))
