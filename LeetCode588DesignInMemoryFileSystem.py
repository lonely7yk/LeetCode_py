"""
Design an in-memory file system to simulate the following functions:

ls: Given a path in string format. If it is a file path, return a list that only contains this 
file's name. If it is a directory path, return the list of file and directory names in this 
directory. Your output (file and directory names together) should in lexicographic order.

mkdir: Given a directory path that does not exist, you should make a new directory according 
to the path. If the middle directories in the path don't exist either, you should create them 
as well. This function has void return type.

addContentToFile: Given a file path and file content in string format. If the file doesn't exist, 
you need to create that file containing given content. If the file already exists, you need to 
append given content to original content. This function has void return type.

readContentFromFile: Given a file path, return its content in string format.

Example:

Input: 
["FileSystem","ls","mkdir","addContentToFile","ls","readContentFromFile"]
[[],["/"],["/a/b/c"],["/a/b/c/d","hello"],["/"],["/a/b/c/d"]]

Output:
[null,[],null,null,["a"],"hello"]

Explanation:
filesystem
 
Note:

You can assume all file or directory paths are absolute paths which begin with / and do not end with / except that the path is just "/".
You can assume that all operations will be passed valid parameters and users will not attempt to retrieve file content or list a directory or file that does not exist.
You can assume that all directory names and file names only contain lower-case letters, and same names won't exist in the same directory.
"""

class FileNode:
    def __init__(self):
        self.isDir = True
        self.children = collections.defaultdict(FileNode)
        self.content = ''
        
# 有点类似于字典树
class FileSystem:

    def __init__(self):
        self.root = FileNode()

    def ls(self, path: str) -> List[str]:
        # 获取 / 之后的所有路径名称
        words = path.split('/')[1:] if path != '/' else []
        p = self.root
        for word in words:
            p = p.children[word]
            
        # 如果 p 是文件夹，返回排序后的 p.children.keys
        # 否则返回路径的最后一个名称
        if p.isDir: return sorted(list(p.children.keys()))
        else: return [words[-1]]

    def mkdir(self, path: str) -> None:
        words = path.split('/')[1:] if path != '/' else []
        p = self.root
        for word in words:
            p = p.children[word]
        
    def addContentToFile(self, filePath: str, content: str) -> None:
        words = filePath.split('/')[1:] if filePath != '/' else []
        p = self.root
        for word in words:
            p = p.children[word]
            
        # p 不是文件夹
        p.isDir = False
        # 追加内容
        p.content += content

    def readContentFromFile(self, filePath: str) -> str:
        words = filePath.split('/')[1:] if filePath != '/' else []
        p = self.root
        for word in words:
            p = p.children[word]
            
        return p.content


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.ls(path)
# obj.mkdir(path)
# obj.addContentToFile(filePath,content)
# param_4 = obj.readContentFromFile(filePath)