from .lcd_i2c import lcd_init
from .lcd_i2c import lcd_string
from .lcd_i2c import LCD_LINE_1
from .lcd_i2c import LCD_LINE_2

from std_msgs.msg import String
import rospy


class DisplayNode():
    def __init__(self):
        rospy.init_node("display_node")
        rospy.loginfo("Setting up display node")
        lcd_init()
        rospy.loginfo("Display initialised and ready for use")
        self.sub = rospy.Subscriber("/message", String, self.display_text)
  
    def wait_for_finish(self):
        rospy.spin()
        
    def display_text(self, msg):
        msg1 = "                "
        msg2 = "                "
        if len(msg.data) > 16:
            msg1 = str(msg.data[0:15])
            msg2 = str(msg.data[16:])
        else:
            msg1 = msg.data
        lcd_string(msg1, LCD_LINE_1)
        lcd_string(msg2, LCD_LINE_2)
  
if __name__ == '__main__':
    main()
