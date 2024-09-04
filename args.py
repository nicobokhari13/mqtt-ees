import argparse

parser = argparse.ArgumentParser()

#-db DATABASE -u USERNAME -p PASSWORD -size 20000
parser.add_argument("-host", "--hostname", dest = "hostname", default = "xyz.edu", help="Server name")
parser.add_argument("-db", "--database", dest = "db", default = "ding_dong", help="Database name")
parser.add_argument("-u", "--username",dest ="username", help="User name")
parser.add_argument("-p", "--password",dest = "password", help="Password")
parser.add_argument("-size", "--binsize",dest = "binsize", help="Size", type=int)

args = parser.parse_args()

print( "Hostname {} db {} User {} Password {} size {} ".format(
        args.hostname,
        args.db,
        args.username,
        args.password,
        args.binsize
        ))
def ConnectToDB():
    print ('Trying to connect to mySQL server')
    # Try to connect to the database
    try:
        con=sql.connect(host=args.hostname, user= args.username, passwd= args.password)
        print ('\nConnected to Database\n')

    # If we cannot connect to the database, send an error to the user and exit the program.
    except sql.Error:
        print ("Error %d: %s" % (sql.Error.args[0],sql.Error.args[1]))
        sys.exit(1)

    return con