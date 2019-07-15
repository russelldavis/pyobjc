# This file is generated by objective.metadata
#
# Last update: Mon Jul 15 07:51:32 2019

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
constants = '''$$'''
enums = '''$OSLogEntryLogLevelDebug@1$OSLogEntryLogLevelError@4$OSLogEntryLogLevelFault@5$OSLogEntryLogLevelInfo@2$OSLogEntryLogLevelNotice@3$OSLogEntryLogLevelUndefined@0$OSLogEntrySignpostTypeEvent@3$OSLogEntrySignpostTypeIntervalBegin@1$OSLogEntrySignpostTypeIntervalEnd@2$OSLogEntrySignpostTypeUndefined@0$OSLogEntryStoreCategoryLongTerm1@4$OSLogEntryStoreCategoryLongTerm14@7$OSLogEntryStoreCategoryLongTerm3@5$OSLogEntryStoreCategoryLongTerm30@8$OSLogEntryStoreCategoryLongTerm7@6$OSLogEntryStoreCategoryLongTermAuto@3$OSLogEntryStoreCategoryMetadata@1$OSLogEntryStoreCategoryShortTerm@2$OSLogEntryStoreCategoryUndefined@0$OSLogEnumeratorReverse@1$OSLogMessageComponentArgumentCategoryData@1$OSLogMessageComponentArgumentCategoryDouble@2$OSLogMessageComponentArgumentCategoryInt64@3$OSLogMessageComponentArgumentCategoryString@4$OSLogMessageComponentArgumentCategoryUInt64@5$OSLogMessageComponentArgumentCategoryUndefined@0$'''
misc.update({})
r = objc.registerMetaDataForSelector
objc._updatingMetadata(True)
try:
    r(b'NSObject', b'activityIdentifier', {'required': True, 'retval': {'type': b'Q'}})
    r(b'NSObject', b'category', {'required': True, 'retval': {'type': b'@'}})
    r(b'NSObject', b'components', {'required': True, 'retval': {'type': b'@'}})
    r(b'NSObject', b'formatString', {'required': True, 'retval': {'type': b'@'}})
    r(b'NSObject', b'process', {'required': True, 'retval': {'type': b'@'}})
    r(b'NSObject', b'processIdentifier', {'required': True, 'retval': {'type': b'i'}})
    r(b'NSObject', b'sender', {'required': True, 'retval': {'type': b'@'}})
    r(b'NSObject', b'subsystem', {'required': True, 'retval': {'type': b'@'}})
    r(b'NSObject', b'threadIdentifier', {'required': True, 'retval': {'type': b'Q'}})
finally:
    objc._updatingMetadata(False)
expressions = {}

# END OF FILE
