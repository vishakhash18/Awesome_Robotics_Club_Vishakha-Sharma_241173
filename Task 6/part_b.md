# PART-B: Failure Recovery Scenario

## Scenario
The **right track** of StepXplorer stops mid-climb due to a motor fault while ascending a staircase.

## Immediate Effects
When the right track fails:
- **Veering Left**: The left track continues moving, causing the robot to turn left unintentionally, creating a curved path.
- **Stability Threat**: Uneven movement shifts the robot’s balance, risking a tip-over on steep stairs.
- **Climbing Disruption**: The robot may stall or fall if it can’t maintain a straight path.

## Fault Detection
StepXplorer identifies the issue using:
- **Motor Encoders**: The right encoder shows zero rotation (no ticks), while the left encoder shows normal activity, indicating a fault.
- **IMU**: Detects unexpected leftward yaw (rotation), signaling unintended turning.
- **Current Sensing**: The right motor may show high current draw (stall condition), which the Arduino can monitor.

## Recovery Strategies
To recover, StepXplorer uses these steps:
1. **Stop Immediately**: The Arduino halts both motors upon detecting an encoder mismatch to avoid further imbalance.
2. **Test Torque**: Briefly boosts power to the right motor to try freeing it (e.g., if it’s a temporary jam).
3. **Pivot Trick**: Runs the left track slowly to pivot the robot clockwise, either realigning it with the stairs (e.g., 20–30° pivot) or turning it to face downward (90° pivot) for retreat.
4. **Backtrack**: If pivoting fails, reverses the left track to return to a flat surface (previous step or floor).
5. **User Alert**: Activates a buzzer or LED to signal the fault.
6. **Continuous Monitoring**: The IMU and encoders provide real-time data to adjust pivoting or backtracking, stopping if tilt exceeds 15° to prevent tipping.

## Example Recovery
- **Detection**: Encoders show right track stopped; IMU detects 10° left yaw.
- **Action**: Arduino pauses, tries torque boost (fails), then pivots left track for 0.5 seconds (200 ticks) to realign.
- **Check**: IMU confirms alignment; if not, reverses to safety.
- **Outcome**: Robot either resumes climbing or retreats without falling.

This strategy uses sensors and the working track to recover safely, protecting StepXplorer from damage.