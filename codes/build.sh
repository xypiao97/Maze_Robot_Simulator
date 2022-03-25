echo target file: $1

MACH_CODE=$1.o
LIB_FILE="lib.$1.so"

g++ -c -fPIC $1 -o $MACH_CODE
g++ -shared -Wl,-soname,$LIB_FILE -o $LIB_FILE $MACH_CODE
rm $MACH_CODE