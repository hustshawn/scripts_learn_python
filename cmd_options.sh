# This script para is a guide to write a script with options


interactive=
filename=~/system_page.html

while [ "$1" != "" ]; do
    case $1 in
        -f | --file )           shift
                                filename=$1
                                ;;
        -i | --interactive )    interactive=1
                                ;;
        -h | --help )           usage
                     
					 exit
                                ;;
        * )                     usage
                                exit 1
    esac
    shift
	# shift [N] to remove previous N paras.
done
