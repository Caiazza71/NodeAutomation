import rclpy
from rclpy.node import Node
from message import Message
from {msgFile.msg} import {msgNames}

class NodeSub(Node):
    def __init__(self):
        super().__init__("{NodeName}")

        # looping through the inputted message array
        for message in {MessageArray}:
            messageName = message.getName()
            topicName = message.getTopic()
            
            # publishing message
            if message.getPubSub() == "Publish":
                self.{messageName} = self.create_publisher(messageName,
                                                         topicName,
                                                         10)
            
            # subscribing to message
            elif message.getPubSub() == "Subscribe":
                 self.{messageName} = self.create_subscription(messageName,
                                                   topicName,
                                                   self.cb, 
                                                   10)
        self.got = 0
    
    def cb(self, msg):
        self.states = msg
        self.got = 1
        self.control()

    def control():
        # blah
        # need to figure out best way to abstract this for dynamic node creation
        # will implement later on when we have a better understanding of process flow
        pass
    
def main(args=None):
    rclpy.init(args=args)  # Initialize ROS2
    print("Initialized ROS2");
    nodesub = NodeSub() # Create the node.
    print("Created node");
    print("Spinning...");
    rclpy.spin(nodesub)  # To keep the node continuously running
                         # and to keep the callbacks re-executing.
    rclpy.shutdown()
    print("Shutdown");
    
if __name__ == '__main__':
    main()