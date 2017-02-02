 """
 
 +Author: Sam Pych
 +Credit: none
  
  Assignment:
  
 @@ -27,8 +27,27 @@
  from ggame import App, Color, LineStyle, Sprite, RectangleAsset, CircleAsset, EllipseAsset, PolygonAsset
  
  # add your code here \/  \/  \/
 -
 -
 +red = Color(0xff0000, 1.0)
 +green = Color(0x00ff00, 1.0)
 +blue = Color(0x0000ff, 1.0)
 +black = Color(0x000000, 1.0)
 +thinline= LineStyle(1, black)
 +circle=CircleAsset(200, thinline, green)
 +rectangle=RectangleAsset(400, 100, thinline, black)
 +ellipse=EllipseAsset(200, 50, thinline, blue)
 +polygon=PolygonAsset([(800, 500),(700, 700),(900, 700),(800, 500)], thinline, black)
 +Sprite(circle, (400,400))
 +Sprite(circle, (1200,400))
 +Sprite(rectangle, (600,800))
 +Sprite(ellipse, (400,50))
 +Sprite(ellipse, (1200,50))
 +Sprite(polygon)
 +circle=CircleAsset(50, thinline, red)
 +Sprite(circle, (400,400))
 +Sprite(circle, (1200,400))
 +circle=CircleAsset(10, thinline, red)
 +Sprite(circle, (720,690))
 +Sprite(circle, (880, 690))
  # add your code here /\  /\  /\
