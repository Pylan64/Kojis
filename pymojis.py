from flask import Flask, render_template
import turtle
#Emoji Amazing

class faces():
    def happyface():
     return '😀'


    def sadface():
        return '😥'


    def angryface():
        return '🤬'


    def moneyface():
        return '🤑'
#1.2
    def poop():
        return '💩'

    def skull():
        return '💀'

    def ghost():
        return '☠'

#1.3    

    def binary():
        return '�'
    
    def smiling_face_with_sunglasses():
        return '😎'
    
    def wrapped_gift():
        return '🎁'
    
    def birthday_cake():
        return '🎂'
    
    def man_shrugging():
        return '🤷‍♂️'
    
    def earth():
        return '🌍'
    
    def earth_americas():
        return '🌍'
    
    def python():
        return '🐍'
    
    def party_popper():
        return '🎉'
    
    def rose():
        return '🌹'
   
    
class emoticons():
    
    def smiley_face():
        return ':)'
    
    def sad_face():
        reuturn ':('
        
    def laughing1():
        return ':D'
    
    def laughing2():
        return 'XD
    
    def laughing3():
        return '8D'
    
    def very_happy_or_double_chin ():
        return ':-))'
    
    def sad():
        return ':('
    
    def sadness():
        return 'D:'
    
    def suprise():
        return ':O'
    
    def wink():
        return ';)'
    
#1.4

class blastoff:
    
    #Blastoof's server code will be here!
    def __init__(self, file):
        self.file = file
        
    app = Flask(__name__)

    @app.route('/')
    def render():
        return render_template(file)

    if __name__=='__main__':
        app.run(debug=True)


class Polygon:
    def __init__(self, size, sides, name="NoName!"):
        self.sides = sides
        self.name = name
        self.size = size
        self.interior_angles = (self.sides-2) * 180
        self.angle = self.interior_angles / self.sides

    def draw(self):
        for i in range(self.sides):
            turtle.forward(self.size)
            turtle.right(180 - self.angle)
        turtle.done
        
