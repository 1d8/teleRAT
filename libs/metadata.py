import stat, time, os

def retrieveMetadata(filepath):
    statObject = os.stat(filepath)
    if statObject != None:
        modificationTime = time.ctime(statObject[stat.ST_MTIME])
        sizeInMegaBytes = statObject[stat.ST_SIZE]/1048576
        lastAccessTime = time.ctime(statObject[stat.ST_ATIME])
        fileMetadata = "Last modified: {}\n".format(modificationTime) + "Size in MB: {}\n".format(str(sizeInMegaBytes)) + "Last accessed: {}\n".format(lastAccessTime)
        return fileMetadata
    return None    
