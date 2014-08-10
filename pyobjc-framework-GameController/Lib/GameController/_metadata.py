# This file is generated by objective.metadata
#
# Last update: Sun Aug 10 22:22:18 2014

import objc, sys

if sys.maxsize > 2 ** 32:
    def sel32or64(a, b): return b
else:
    def sel32or64(a, b): return a
if sys.byteorder == 'little':
    def littleOrBig(a, b): return a
else:
    def littleOrBig(a, b): return b

misc = {
}
misc.update({'GCExtendedGamepadSnapShotDataV100': objc.createStructType('GCExtendedGamepadSnapShotDataV100', b'{_GCExtendedGamepadSnapShotDataV100=SSffffffffffffff}', sel32or64(['version'], ['size'], ['dpadX'], ['dpadY'], ['buttonA'], ['buttonB'], ['buttonX'], ['buttonY'], ['leftShoulder'], ['rightShoulder'], ['leftThumbstickX'], ['leftThumbstickY'], ['rightThumbstickX'], ['rightThumbstickY'], ['leftTrigger'], ['rightTrigger']), None, 1), 'GCExtendedGamepadValueChangedHandler': objc.createStructType('GCExtendedGamepadValueChangedHandler', b'{_GCGamepadSnapShotDataV100=SSffffffff}', ['version', 'size', 'dpadX', 'dpadY', 'buttonA', 'buttonB', 'buttonX', 'buttonY', 'leftShoulder', 'rightShoulder']), 'GCGamepadSnapShotDataV100': objc.createStructType('GCGamepadSnapShotDataV100', b'{_GCGamepadSnapShotDataV100=SSffffffff}', ['version', 'size', 'dpadX', 'dpadY', 'buttonA', 'buttonB', 'buttonX', 'buttonY', 'leftShoulder', 'rightShoulder'])})
constants = '''$GCControllerDidConnectNotification$GCControllerDidDisconnectNotification$'''
enums = '''$GCControllerPlayerIndexUnset@-1$'''
misc.update({})
functions={'NSDataFromGCGamepadSnapShotDataV100': (b'@^{_GCGamepadSnapShotDataV100=SSffffffff}',), 'NSDataFromGCExtendedGamepadSnapShotDataV100': (b'@^{_GCExtendedGamepadSnapShotDataV100=SSffffffffffffff}',), 'GCGamepadSnapShotDataV100FromNSData': (b'Z^{_GCGamepadSnapShotDataV100=SSffffffff}@',), 'GCExtendedGamepadSnapShotDataV100FromNSData': (b'Z^{_GCExtendedGamepadSnapShotDataV100=SSffffffffffffff}@',)}
r = objc.registerMetaDataForSelector
objc._updatingMetadata(True)
try:
    r(b'GCController', b'isAttachedToDevice', {'retval': {'type': b'Z'}})
    r(b'GCControllerButtonInput', b'isPressed', {'retval': {'type': b'Z'}})
    r(b'GCControllerElement', b'isAnalog', {'retval': {'type': b'Z'}})
finally:
    objc._updatingMetadata(False)
expressions = {}

# END OF FILE
