# The Ugly Duckling

Autonomous Mars Robot to pick up targets and deliver to the mothership while avoiding obstacles. Competed at the 2019 IEEE R5 Autonomous Robotics Competition. Medium Article: https://medium.com/@rishavrajendra/autonomous-mars-rover-using-raspberry-pi-arduino-and-pi-camera-5b285be452c1

Video of the robot in action: https://www.youtube.com/watch?v=3CT76dNDTTw&feature=youtu.be

![alt text](https://github.com/RishavRajendra/TheUglyDuckling/blob/master/pictures/playingField.png)

## Details

These batteries were used to power the robot: https://www.batteryspace.com/samsung-lithium-18650-rechargeable-cell-3-7v-1500mah-5-55wh-23a-rate---inr18650-15m---un-38-3-passed.aspx


### MR. W Motor Controller Board by [Wade Rivero](https://www.linkedin.com/in/wade-rivero-60ab64101/)
![alt text](https://github.com/RishavRajendra/TheUglyDuckling/blob/master/pictures/MrWboard.png)

### Execution

0. Compile and upload the arduino code
```
cd motion/
make
make upload
```

1. Launch the main script on the Raspberry Pi. The robot will try and navigate around the field to pick up targets and drop it in the mothership. The Tensorflow model will take around 30 seconds to boot up.
```
python3 main.py
```

## Installation

### Prerequisites

Tested on Python 3.5.3

```
pip install pySerial
pip install keyboard
pip install tensorflow
pip install numpy
pip install pandas
```

Follow tutorials from [Edje Electronics](https://github.com/EdjeElectronics/TensorFlow-Object-Detection-API-Tutorial-Train-Multiple-Objects-Windows-10) and [Sendtex](https://www.youtube.com/watch?v=COlbP62-B-U&list=PLQVvvaa0QuDcNK5GeCQnxYnSSaar2tpku) to train your own object detection model.

## Contributors

#### Programming

* **Rishav Rajendra** - [Website](https://rishavrajendra.github.io)
* **Benji Lee**
* **Michael Ceraso** - [Linkedin](https://www.linkedin.com/in/soceraso/)
* **Dylan Vo** - [Linkedin](https://www.linkedin.com/in/dylan-vo-a885231a4/)
* **Tony Le** - [Linkedin](https://www.linkedin.com/in/tony-le-a73a96199/)

#### Mechanical

* **James Winnert** - [Linkedin](https://www.linkedin.com/in/jameswinnert/)
* **Suzanne Ly**

#### Motor Controller Board and Electrical

* **Michael Ceraso** - [Linkedin](https://www.linkedin.com/in/soceraso/)
* **Wade Rivero** - [Linkedin](https://www.linkedin.com/in/wade-rivero-60ab64101/)
* **Rishav Rajendra (Explosive Electrical)**
* **Dylan Vo** - [Linkedin](https://www.linkedin.com/in/dylan-vo-a885231a4/)
* **Tony Le** - [Linkedin](https://www.linkedin.com/in/tony-le-a73a96199/)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
