from flask import Flask, render_template, request

app = Flask(__name__)
app.config['DEBUG'] = True

def valid_hex_chars(hex):
   for char in hex.upper():  
      if char not in '0123456789ABCDEF':
         return False  
   return True

@app.route('/hex_form', methods=["GET", "POST"])
def hex_form():
   if request.method == 'POST':
      hex = request.form['hex']      
      if hex and hex.startswith('#'):
            hex = hex[1:]       
      if len(hex) != 6:
         feedback = "Hex code must contain exactly 6 characters."
         hex = '0000FF'
      elif not valid_hex_chars(hex):
            feedback = "Invalid hex color! Please use only digits (0-9) and letters (A-F)."
            hex = '00FF00'
      else:
            feedback = "Invalid hex color! Please use only digits (0-9) and letters (A-F)."
            hex = 'FF0000' 
   else:
      hex = '987654'
      feedback = "Display here..."

   return render_template('hex_form.html', hex=hex, feedback=feedback)

if __name__ == '__main__':
    app.run()

# Find the exercise instructions here:
# https://education.launchcode.org/lchs/chapters/flask-intro/exercises.html
