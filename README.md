# Billee Bot
This repository is designed to store all urdf files and launch scripts

## Launch Files

### State Publisher:

```bash
ros2 launch billee_bot rsp.launch.py
```

#### Argument: use_sim_time

```bash
ros2 launch billee_bot rsp.launch.py use_sim_time:=true
```

#### Description:
Boolean for when you use this on a real robot or in a simulation  

Default: False

