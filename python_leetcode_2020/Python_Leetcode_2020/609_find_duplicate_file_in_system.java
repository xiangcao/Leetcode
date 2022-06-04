609. Find Duplicate File in System
"""
Given a list of directory info including directory path, and all the files with contents in this directory, you need to find out all the groups of duplicate files in the file system in terms of their paths.

A group of duplicate files consists of at least two files that have exactly the same content.

A single directory info string in the input list has the following format:

"root/d1/d2/.../dm f1.txt(f1_content) f2.txt(f2_content) ... fn.txt(fn_content)"

It means there are n files (f1.txt, f2.txt ... fn.txt with content f1_content, f2_content ... fn_content, respectively) in directory root/d1/d2/.../dm. Note that n >= 1 and m >= 0. If m = 0, it means the directory is just the root directory.

The output is a list of group of duplicate file paths. For each group, it contains all the file paths of the files that have the same content. A file path is a string that has the following format:

"directory_path/file_name.txt"

Example 1:

Input:
["root/a 1.txt(abcd) 2.txt(efgh)", "root/c 3.txt(abcd)", "root/c/d 4.txt(efgh)", "root 4.txt(efgh)"]
Output:  
[["root/a/2.txt","root/c/d/4.txt","root/4.txt"],["root/a/1.txt","root/c/3.txt"]]
 

Note:

No order is required for the final output.
You may assume the directory name, file name and file content only has letters and digits, and the length of file content is in the range of [1,50].
The number of files given is in the range of [1,20000].
You may assume no files or directories share the same name in the same directory.
You may assume each given directory info represents a unique directory. Directory path and file info are separated by a single blank space.
 

Follow-up beyond contest:
Imagine you are given a real file system, how will you search files? DFS or BFS?
If the file content is very large (GB level), how will you modify your solution?
If you can only read the file by 1kb each time, how will you modify your solution?
What is the time complexity of your modified solution? What is the most time-consuming part and memory consuming part of it? How to optimize?
How to make sure the duplicated files you find are not false positive?
"""
Python:
class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        contentToFiles = collections.defaultdict(list)
        for path in paths:
            values = path.split(" ")
            root_path = values[0]
            for file in values[1:]:
                name_contents = file.split('(');
                name = name_contents[0]
                content = name_contents[1][:-1]
                contentToFiles[content].append(root_path + '/' + name)
        
        return [files for files in contentToFiles.values() if len(files) > 1]

class Solution {
    public List<List<String>> findDuplicate(String[] paths) {
        HashMap<String, List<String>> map = new HashMap<>();
        for (String path: paths) {
            String [] values = path.split(" ");
            String rootPath = values[0];
            for ( int i = 1; i < values.length; i++) {
                String[] name_content = values[i].split("\\(");
                name_content[1] = name_content[1].replace(")", "");
                List<String> dupFileList = map.getOrDefault(name_content[1], new ArrayList<String>());
                dupFileList.add(values[0] + "/" + name_content[0]);
                map.put(name_content[1], dupFileList);
            }
        }

        List<List<String>> result = new ArrayList<>();
        for(List<String> value: map.values()) {
            if (value.size() > 1) {
                result.add(value);
            }
        }
        return result8;
    }
}

************************************
https://leetcode.com/problems/find-duplicate-file-in-system/discuss/104120/Follow-up-questions-discussion
https://www.cnblogs.com/beiyeqingteng/p/11257559.html
Simonzhu91:
In preparing for my Dropbox interview, I came across this problem and really wanted to find the ideas behind the follow up questions (as these were the questions that the interviewer was most interested in, not the code itself). Since this is the only post with the follow up discussion, i'll comment here! @yujun gave a great solution above and I just wanted to add a bit more to help future interviewees.

To find duplicate files, given input of String array is quite easy. Loop through each String and keep a HashMap of Strings to Set/Collection of Strings: mapping the contents of each file to a set of paths with filename concatenated.

For me, instead of given a list of paths, I was given a Directory and asked to return List of List of duplicate files for all under it. I chose to represent a Directory like:

class Directory{
     List<Directory> subDirectories;
     List<File> files;
}
Given a directory, you are asked how you can find duplicate files given very large files. The idea here is that you cannot store contents in memory, so you need to store the file contents in disk. So you can hash each file content and store the hash as a metadata field for each file. Then as you perform your search, store the hash instead the file's contents in memory. So the idea is you can do a DFS through the root directory and create a HashMap<String, Set<String>> mapping each hash to the Set of filepaths + filenames that correspond to that hash's content.

(Note: You can choose BFS / DFS to traverse the Path. I chose DFS as it is more memory efficient and quicker to code up.)

Follow Up: This is great, but it requires you to compute the hash for every single file once, which can be expensive for large files. Is there anyway you can avoid computing the hash for a file?

One approach is to also maintain a metadata field for each file's size on disk. Then you can take a 2 pass approach:

DFS to map each size to a set of paths that have that size
For each size, if there are more than 2 files there, compute hash of every file, if any files with the same size have the same hash, then they are identical files.
This way, you only compute hashes if you have multiple files with the same size. So when you do a DFS, you can create a HashMap<Integer, Set<String>>, mapping each file's size to the list of file paths that have that size. Loop through each String in each set, get its hash, check if it exists in your set, if so, add it to your List<String> res otherwise add it into the set. In between each key (switching file sizes), you can add your res to your List<List<String>>.
**************************
Yujun:
Just want to share my humble opinions for discussion:
If anyone has a better solution, I would appreciate it if you'd like to correct and enlighten me:-)
Question 2:
In real-world file system, we usually store large file in multiple "chunks" (in GFS, one chunk is 64 MB),so we have meta data recording the file size,file name and index of different chunks along with each chunk's checkSum (the xor for the content).
So when we upload a file, we record the meta data as mentioned above.
When we need to check for duplicates, we could simply check the meta data:
1.Check if files are of the same size;
2.if step 1 passes, compare the first chunk's checkSum
3.if step 2 passes, check the second checkSum
...
and so on.
There might be false positive duplicates, because two different files might share the same checkSum.

Question 3:
In the way mentioned above, we could read the meta data instead of the entire file, and compare the information KB by KB.

Question 5:
Using checkSum, we could quickly and accurately find out the non-duplicated files. But to totally avoid getting the false positive, we need to compare the content chunk by chunk when we find two "duplicates" using checkSum.

********************
To summarize simonzhu91 and yujun solution, here i post my solution combining with my idea. Welcome people to discuss it deeper together.

Question-1:
Imagine you are given a real file system, how will you search files? DFS or BFS?

Answer:
core idea: DFS
Reason: if depth of directory is not too deeper, which is suitable to use DFS, comparing with BFS.

import java.io.File;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.nio.file.attribute.BasicFileAttributes;

import java.security.MessageDigest;
import java.math.BigInteger;

class Directory {
	List<Directory> subDirectories;
	List<File> files;
}

public static String makeHashQuick(File file) {
	try {
		FileInputStream fileInput = new FileInputStream(file);
		byte[] data = new byte[(int) file.length()];
		fileInput.read(data);
		fileInput.close();

		MessageDigest md = MessageDigest.getInstance("MD5");
		String fileHash = new BigInteger(1, md.digest(data)).toString(16);
		return fileHash;
	} catch (IOException e) {
		throw new RuntimeException("can't read file: " + file.getAbsolutePath(), e);
	}
}

public static void findDuplicatedFilesByMD5FromFile(Map<String, List<String>> lists, File file) {
	String fileHash = makeHashQuick(file)
	List<String> list = lists.get(fileHash);
	if (list==null) {
		list = new LinkedList<String>();
		lists.put(fileHash, list);
	}
	list.add(file.getAbsolutePath());
}

public static void findDuplicatedFilesByMD5(Map<String, List<String>> lists, Directory dir) {
	for (File file: dir.files) {
		findDuplicatedFilesByMD5FromFile(lists, file);
	}
	for (Directory curDir: dir.subDirectories) {
		findDuplicatedFilesByMD5(lists, curDir);
	}
}

public static List<List<String>> storeDuplicateFiles(Directory dir) {
	List<List<String>> ret = new ArrayList<List<String>>();
	Map<String, List<String>> listsByMD5 = new HashMap<String, List<String>>();
	findDuplicatedFilesByMD5(listsByMD5, dir);
	for (List<String> list: listsByMD5) {
		if (list.size()>1) {
			ret.add(list);
		}
	}
	return ret;
}
Question-2:
If the file content is very large (GB level), how will you modify your solution?

Answer:
core idea: make use of meta data, like file size before really reading large content.
Two steps:
DFS to map each size to a set of paths that have that size: Map<Integer, Set>
For each size, if there are more than 2 files there, compute hashCode of every file by MD5, if any files with the same size have the same hash, then they are identical files: Map<String, Set>, mapping each hash to the Set of filepaths+filenames. This hash id's are very very big, so we use the Java library BigInteger.
public static void findDuplicatedFilesBySizeFromFile(Map<Integer, List<String>> lists, File file) {
	try {
		Path filePath = Paths.get(file.getAbsolutePath());
		BasicFileAttributes attr = Files.readAttributes(filePath, BasicFileAttributes.class);
		int size = attr.size();
		List<String> list = lists.get(size);
		if (list==null) {
			list = new LinkedList<String>();
			lists.put(size, list);
		}
		list.add(file.getAbsolutePath());
	} catch (IOException e) {
		throw new RuntimeException("can't read file attributes: " + file.getAbsolutePath(), e);
	}
}

public static void findDuplicatedFilesBySize(Map<Integer, List<String>> lists, Directory dir) {
	for (File file: dir.files) {
		findDuplicatedFilesBySizeFromFile(lists, file);
	}
	for (Directory curDir: dir.subDirectories) {
		findDuplicatedFilesBySize(lists, curDir);
	}
}

public static List<List<String>> storeDuplicateFiles(Directory dir) {
	List<List<String>> ret = new ArrayList<List<String>>();
	Map<Integer, List<String>> listsBySize = new HashMap<Integer, List<String>>();
	findDuplicatedFilesBySize(listsBySize, dir);
	Map<String, List<String>> listsByMD5 = new HashMap<String, List<String>>)();
	for (List<String> list: listsBySize) {
		if (list.size()>1) {
			for (String fileName: list) {
				findDuplicatedFilesByMD5FromFile(listsByMD5, new File(fileName));
			}
		}
	}
	for (List<String> list: listsByMD5) {
		if (list.size()>1) {
			ret.add(list);
		}
	}
	return ret;
}
To optimize Step-2. In GFS, it stores large file in multiple "chunks" (one chunk is 64KB). we have meta data, including the file size, file name and index of different chunks along with each chunk's checkSum(the xor for the content). For step-2, we just compare each file's checkSum.
Disadvantage: there might be flase positive duplicates, because two different files might share the same checkSum.
Question-3:
If you can only read the file by 1kb each time, how will you modify your solution?

Answer:
makeHashQuick Function is quick but memory hungry, might likely to run with java -Xmx2G or the likely to increase heap space if RAM avaliable.
we might need to play with the size defined by "buffSize" to make memory efficient.
import java.io.RandomAccessFile;

public static String makeHashLean(File infile) {
	RandomAccessFile file = new RandomAccessFile(infile, "r");
	int buffSize = 1024;
	byte[] buffer = new byte[buffSize];
	// calculate the hash of the whole file
	long offset = file.length();
	long read = 0;
	int unitsize;
	while(read<offset) {
		unitsize = (int) (((offset-read)>=buffSize)?buffSize:(offset-read));
		file.read(buffer, 0, unitsize);
		md.update(buffer, 0, unitsize);
		read += unitsize;
	}
	file.close();
	String hash = new BigInteger(1, md.digest()).toString(16);
	return hash;
}
Question-4:
What is the time complexity of your modified solution? What is the most time-consuming part and memory consuming part of it? How to optimize?

Answer:
hashing part is the most time-consuming and memory consuming.
optimize as above mentioned, but also introduce false positive issue.
Question-5:
How to make sure the duplicated files you find are not false positive?

Answer:
Question-2-Answer-1 will avoid it.
We need to compare the content chunk by chunk when we find two "duplicates" using checkSum.


******************************
# https://leetcode.com/problems/find-duplicate-file-in-system/discuss/104123/C%2B%2B-clean-solution-answers-to-follow-up

Follow up questions:

1. Imagine you are given a real file system, how will you search files? DFS or BFS ?
In general, BFS will use more memory then DFS. However BFS can take advantage of the locality of files in inside directories, and therefore will probably be faster

2. If the file content is very large (GB level), how will you modify your solution?
In a real life solution we will not hash the entire file content, since it's not practical. Instead we will first map all the files according to size. Files with different sizes are guaranteed to be different. We will than hash a small part of the files with equal sizes (using MD5 for example). Only if the md5 is the same, we will compare the files byte by byte

3. If you can only read the file by 1kb each time, how will you modify your solution?
This won't change the solution. We can create the hash from the 1kb chunks, and then read the entire file if a full byte by byte comparison is required.

What is the time complexity of your modified solution? What is the most time consuming part and memory consuming part of it? How to optimize?
Time complexity is O(n^2 * k) since in worse case we might need to compare every file to all others. k is the file size

How to make sure the duplicated files you find are not false positive?
We will use several filters to compare: File size, Hash and byte by byte comparisons.
*********************************************************************************************
Thanks for writing this awesome answer and your response to the follow-up questions,
I just wanted to make up a few points that you missed:

MD5 is definitely one way to hash a file, another more optimal alternative is to use SHA256. Reference

Also, to answer this What is the most time consuming part and memory consuming part of it? How to optimize? part:
Comparing the file (by size, by hash and eventually byte by byte) is the most time consuming part.
Generating hash for every file will be the most memory consuming part.
We follow the above procedure will optimize it, since we compare files by size first, only when sizes differ, we'll generate and compare hashes, and only when hashes are the same, we'll compare byte by byte.
Also, using better hashing algorithm will also reduce memory/time.
Reference
