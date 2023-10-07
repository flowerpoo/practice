from flask import Flask, render_template
app=Flask(__name__)

"""products={
    1: {'name':"product 1", 'price': 12, "description":"1st description",'image':'image 1'},
   2: {'name':"product 2", 'price': 22, "description":"2nd description",'image':'image 2'},
    3:{'name':"product 3", 'price': 33, "description":"3rd description",'image':'image 3'},

}"""
cart={}
@app.route('/')

def display_products():
    return render_template('products.html', products=products)

@app.route('/cart/add/<product_id>')
def add_cart(product_id ):
   product=products.get(product_id) 
   return render_template('product.html',products=products, product_id=product_id)
   """
   if product:
        user__id=get_user_session_id()
        if user__id in product:
           cart[user__id].append(product)
        else:
            cart[user__id]=[product]
        return "product added succesfully"
   else:
        return "product not found " """
   

if __name__ == '__main__':
    app.run(debug=True)