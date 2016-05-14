import ConfigParser

config = ConfigParser.SafeConfigParser()

# When adding sections or items, add them in the reverse order of
# how you want them to be displayed in the actual file.
# In addition, please note that using RawConfigParser's and the raw
# mode of ConfigParser's respective set functions, you can assign
# non-string values to keys internally, but will receive an error
# when attempting to write to a file or when you get it in non-raw
# mode. SafeConfigParser does not allow such assignments to take place.
#config.add_section('Section1')
#config.set('Section1', 'an_int', '15')
#config.set('Section1', 'a_bool', 'true')
#config.set('Section1', 'a_float', '3.1415')
#config.set('Section1', 'baz', 'fun')
#config.set('Section1', 'bar', 'Python')
#config.set('Section1', 'foo', '%(bar)s is %(baz)s!')
config.read('example.cfg')
#
if config.has_section('Linux'):
    i = 20
    print config.sections()
    while i < 30 :
        config.set('Linux','wwn'+str(i),"12345678")
        config.options('Linux')
        i += 1
else :
    config.add_section('Linux')
    i = 10
    print config.sections()
    while i < 20 :
        config.set('Linux','wwn'+str(i),"12345678")
        config.options('Linux')
        i += 1
#
# Writing our configuration file to 'example.cfg'
with open('example.cfg', 'a') as configfile:
    config.write(configfile)

#c = ConfigParser.SafeConfigParser.set('Linux','wwn'+str(i),"12345678")

