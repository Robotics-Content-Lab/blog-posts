# Publisher and Subscriber Example

This is a basic example that implements a publisher and two subscribers using the ROS2 library. The publisher sends a message on the `chatter` topic, the subscribers log this message to the screen by subscribing to the topic.

## How to run

Open a terminal and run the following command to start the publisher:

```bash
cd ~/ros2_ws
colcon build --packages-select pub_sub --symlink-install
source install/setup.bash
ros2 run pub_sub publisher
```

<figure>
    <center>
    <img src="rosgraph.png" alt="Publisher + 2 Subscribers on the chatter topic">
    </center>
    <caption>The publisher `publisher` publishes on the topic `/chatter` and the two subscribers (`subscriber1`, `subscriber2`) listen on that topic</caption>
</figure>