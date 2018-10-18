def sorting ():
	file = open("Emotions_db.txt","r");
	inFile = open ("raw_data.txt", "r");
	#outFile = open ("filtered_data.txt", "r");
	lines1 = [line.lower() for line in inFile];
	with open ("raw_data.txt", "w") as out:
		out.writelines(sorted(lines1));
	lines0 = [line.lower() for line in file];
	with open ("Emotions_db.txt", "w") as out:
		out.writelines(sorted(lines0));
	#lines2 = [line.lower() for line in outFile];
	#with open ("filtered_data.txt", "w") as out:
	#	out.writelines(sorted(lines2));

def emofilterlabel () :
	outFile = open ("filtered_data.txt", "w");  #outfile
	buffer = [];
	with open('raw_data.txt') as f_a, open('Emotions_db.txt') as f_b:
    		a_lines = set(f_a.read().splitlines())
    		b_lines = set(f_b.read().splitlines())
	for line in a_lines:
    		print(line, '->', line in b_lines);
		if line in b_lines:
			buffer.append(line);
			buffer.append("\n");
	outFile.write("".join(buffer));
	
	outFile.close();
from itertools import chain;
from glob import glob;
emofilterlabel ();
#inFile = open ("raw_data.txt", "r");
#outFile = open ("filtered_data.txt", "w");
#buffer = [];
#for line in inFile:
#	buffer.append(line);
#outFile.write("".join(buffer));
#outFile.close();
outFile = open ("filtered_data.txt", "r");
lines2 = [line.lower() for line in outFile];
with open ("filtered_data.txt", "w") as out:
	out.writelines(sorted(lines2));
sorting ();

#inFile.close();
#outFile.close();
out.close();


