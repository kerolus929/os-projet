using System;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Reflection;
using System.IO;
using System.Collections.Generic;

namespace ConsoleApp1
{
    public class command
    {
        public static void check(string x)
        {
            string[] q = x.Split(' ');
            // Console.WriteLine(q.Length);
            if (x == "cls" || x == "CLS")
                Clear();
            else if (x == "quit" || x == "QUIT")
                Quit();
            else if (x == "help" || x == "HELP")
                Help();
            else if (q[0] == "md" || q[0] == "MD")
                MD(q[1]);
            else if (q[0] == "rd" || q[0] == "RD")
                rd(q[1]);
            else if (q[0] == "type" || q[0] == "TYPE")
            {
                for (int i = 1; i < q.Length; i++)
                {
                    type(q[i]);
                }
            }

            else if (q[0] == "del" || q[0] == "DEL")
            {
                for (int i = 1; i < q.Length; i++)
                    delete(q[i]);

            }

            else if (q.Length > 2 && q[0] == "copy")
                copy(q[1], q[2]);

            else if (q[0] == "help" && q.Length > 1)
            {

                if (q[1] == "clear")
                    cls();
                else if (q[1] == "quit")
                    quit();
                else if (q[1] == "help")
                    help();
                else if (q[1] == "md")
                    made();
                else if (q[1] == "rename")
                    rename();
                else if (q[1] == "type")
                    Type();
                else if (q[1] == "rd")
                    remove();
                else if (q[1] == "del")
                    Delete();
                else if (q[1] == "copy")
                    COPY();
                else
                    Console.WriteLine(x + " is not recognized as an internal or external command program or batch file.");

            }
            else if (q.Length > 2 && q[0] == "rename")
                Rename(q[1], q[2]);


            else
                Console.WriteLine(x + " is not recognized as an internal or external command program or batch file.");


            //Console.WriteLine(x + " is not recognized as an internal or external command program or batch file.");


        }
        static void Clear()
        {
            Console.Clear();
        }


        static void Quit()
        {


            Environment.Exit(-1);


            // System.Threading.Thread.Sleep(5000);
        }
        static void MD(string a)
        {

            string dir = $@"D:\{a}";
            // If directory does not exist, create it
            if (!Directory.Exists(dir))
            {
                Directory.CreateDirectory(dir);
            }


        }


        public static void rd(string a)
        {

            string dir = $@"D:\{a}";
            // If directory does not exist, create it
            if (Directory.Exists(dir))
            {
                Directory.Delete(dir);
            }
            else
                Console.WriteLine("the file is not exists");
        }
        public static void Rename(string a, string c)
        {
            rd(a);
            MD(c);
            Console.WriteLine("file is renamed");
        }
        public static void type(string a)
        {
            string[] lines = File.ReadAllLines($@"D:\{a}");

            foreach (string line in lines)
                Console.WriteLine(line);
        }
        public static void copy(string sour, string dest)
        {
            string sourceFile = $@"D:\{sour}";
            string destinationFile = $@"E:\{dest}";

            System.IO.File.Copy(sourceFile, destinationFile);
            Console.WriteLine("the process is done");

        }
        public static void delete(string sour)
        {
            string sourceFile = $@"D:\{sour}";


            System.IO.File.Delete(sourceFile);

        }
        static void Help()
        {

            Console.WriteLine("  CD :       Displays the name of or changes the current directory.");
            Console.WriteLine("  CLS :      Clears the screen.");
            Console.WriteLine("  DIR  :     Displays a list of files and subdirectories in a directory.");
            Console.WriteLine("  EXIT:      Quits the CMD.EXE program (command interpreter).");
            Console.WriteLine("  COPY :     Copies one or more files to another location.");
            Console.WriteLine("  DEL  :     Deletes one or more files.");
            Console.WriteLine("  HELP:      Provides Help information for Windows commands.");
            Console.WriteLine("  MD  :      Creates a directory.");
            Console.WriteLine("  RD  :      Removes a directory.");
            Console.WriteLine("  RENAME:    Renames a file or files.");
            Console.WriteLine("  TYPE  :    Displays the contents of a text file.");

        }
        public static void cls()
        {
            Console.WriteLine();
            Console.WriteLine("CLS            Clears the screen.");
            Console.WriteLine();


        }
        public static void quit()
        {
            Console.WriteLine();
            Console.WriteLine("EXIT           Quits the CMD.EXE program (command interpreter).");
            Console.WriteLine();

        }
        public static void help()
        {
            Console.WriteLine();
            Console.WriteLine("HELP           Provides Help information for Windows commands.");
            Console.WriteLine();

        }
        public static void made()
        {
            Console.WriteLine();
            Console.WriteLine("MD             Creates a directory.");
            Console.WriteLine();

        }
        public static void remove()
        {
            Console.WriteLine();
            Console.WriteLine("RD             Removes a directory.");
            Console.WriteLine();

        }
        public static void rename()
        {
            Console.WriteLine();
            Console.WriteLine("RENAME         Renames a file or files.");
            Console.WriteLine();

        }
        public static void Type()
        {
            Console.WriteLine();
            Console.WriteLine("TYPE           Displays the contents of a text file.");
            Console.WriteLine();

        }
        public static void COPY()
        {
            Console.WriteLine();
            Console.WriteLine("COPY           Copies one or more files to another location.");
            Console.WriteLine();

        }
        public static void Delete()
        {
            Console.WriteLine();
            Console.WriteLine("DEL            Deletes one or more files.");
            Console.WriteLine();

        }

    }
    class Program
    {
       
        public class vertual_disk
        {
            public static void initialize()
            {
                if (!File.Exists(@"E:FAT.txt"))
                {
                    FileStream fs = new FileStream(@"E:FAT.txt", FileMode.OpenOrCreate, FileAccess.ReadWrite);

                    for (int i = 0; i < 1024; i++)
                    {
                        fs.WriteByte(0);
                    }
                    //char y = '*';
                    //string vertualFAT = "";
                    for (int i = 0; i < (1024 * 4); i++)
                    {
                        fs.WriteByte((byte)'*');
                    }
                    //char z = '#';
                    //string vertualfat = "";
                    for (int i = 0; i < (1024 * 1019); i++)
                    {
                        fs.WriteByte((byte)'#');
                    }

                    //File.WriteAllText(path, text + vertualFAT + vertualfat);
                    fs.Flush();
                    fs.Close();
                }
                else
                {
                    Console.WriteLine("the file is exist");
                }
            }
            public static void write_block(byte[] mydata, int index)
            {
                FileStream fs = new FileStream(@"E:\\BIO3 2\\os project\\FAT.txt", FileMode.Open, FileAccess.Write);
                fs.Seek(1024 * index, SeekOrigin.Begin);
                for (int i = 0; i < mydata.Length; i++)
                {
                    fs.WriteByte(mydata[i]);
                }
                fs.Flush();
                fs.Close();
            }
            public static byte[] get_block(int index)
            {
                FileStream fs = new FileStream(@"E:\\BIO3 2\\os project\\FAT.txt", FileMode.Open, FileAccess.Read);
                fs.Seek(index * 1024, SeekOrigin.Begin);
                byte[] byte_ReadText = new byte[1024];
                fs.Read(byte_ReadText, 0, byte_ReadText.Length);
                fs.Flush();
                fs.Close();
                return byte_ReadText;

            }

        }
        public class FAT
        {
            public static int[] fat_table;
            public FAT()
            {
                fat_table = new int[1024];
            }
            public static void initialize()
            {

                for (int i = 0; i < 1024 - 1; i++)
                {
                    if (i <= 4)
                    {
                        fat_table[i] = 1023;
                    }
                    else
                    {
                        fat_table[i] = 0;
                    }
                }

            }
            public static void write_fat_table()
            {
                FileStream fs = new FileStream(@"E:FAT.txt", FileMode.Open, FileAccess.Write);
                fs.Seek(1024, SeekOrigin.Begin);
                byte[] b = new byte[1024 * 4];
                Buffer.BlockCopy(fat_table, 0, b, 0, b.Length);
                fs.Write(b);

                fs.Flush();
                fs.Close();
            }
            public static int[] read_fat_table()
            {
                FileStream fs = new FileStream(@"E:FAT.txt", FileMode.Open, FileAccess.Read);
                fs.Seek(1024, SeekOrigin.Begin);
                byte[] c = new byte[1024 * 4];
                fs.Read(c, 0, c.Length);
                int[] arr = new int[fat_table.Length];
                Buffer.BlockCopy(c, 0, arr, 0, arr.Length);
                fs.Flush();
                fs.Close();

                return arr;
            }
            public static void print_fat_table()
            {
                int[] arr = read_fat_table();
                for (int i = 0; i < 1024; i++)
                {
                    Console.WriteLine($"{i}-----{arr[i]} ");
                }
            }
            public static int get_available_block()
            {
                int i;
                for (i = 0; i < 1024; i++)
                {
                    if (fat_table[i] == 0)
                        break;

                }
                return i;
            }
            public static int get_next(int index)
            {
                Console.WriteLine(fat_table[index]);
                return fat_table[index];
            }
            public static void set_next(int index, int value)
            {
                fat_table[index] = value;
            }
            public static int get_available_blocks()
            {
                int counter = 0;
                for (int i = 0; i < fat_table.Length; i++)
                {
                    if (fat_table[i] == 0)
                        counter++;
                }
                return counter;
            }
        }
        public class Directory_Entry
        {
            public char[] fileName = new char[11];
            byte fileAtterbute;
            int[] fileEmpty = new int[3];
            int fileSize;
            public int firstCluster;
            public Directory_Entry(char[] fileName, byte fileAtterbute, int firstCluster)
            {
                this.fileName = fileName;
                this.fileAtterbute = fileAtterbute;
                this.firstCluster = firstCluster;
            }

            public byte[] get_bytes()
            {
                if (fileName.Length < 11)
                {
                    for (int i = fileName.Length; i < 11; i++)
                    {
                        fileName[i] = ' ';
                    }
                }
                byte[] b = new byte[32];
                byte[] l = Encoding.ASCII.GetBytes(fileName);
                l.CopyTo(b, 0);
                //fileName.CopyTo(b, 0);
                b[11] = fileAtterbute;
                fileEmpty.CopyTo(b, 12);

                return b;
            }
            public void get_Directory_Entry(byte[] b)
            {
                b.CopyTo(fileName, 0);
                fileAtterbute = b[11];
                b.CopyTo(fileEmpty, 12);


            }
        }
        public class Directory : Directory_Entry
        {
            List<Directory_Entry> Directory_table;
            Directory parent;
            public Directory(char[] fileName, byte fileAtterbute, int firstCluster, Directory parent) : base(fileName, fileAtterbute, firstCluster)
            {
                if (parent != null)
                {
                    this.parent = parent;
                }
                Directory_table = new List<Directory_Entry>();
            }
            public void write_Directory()
            {
                byte[] Directory_table_B = new byte[32 * Directory_table.Count()];
                for (int i = 0; i < Directory_table.Count(); i++)
                {
                    byte[] Directory_Entry_B = Directory_table[i].get_bytes();
                    for (int j = i * 32, c = 0; c < 32; j++, c++)
                    {
                        Directory_table_B[j] = Directory_Entry_B[c];
                    }
                }
                int num_full_Size = Directory_table_B.Length / 1024;
                double num_of_required_blocks = Math.Ceiling(Directory_table_B.Length / 1024.0);
                //decimal num_of_full_blocks = Math.Floor(num);
                int reminder = Directory_table_B.Length % 1024;
                if (num_of_required_blocks <= FAT.get_available_blocks())
                {
                    int fat_index;
                    int last_index = -1;
                    if (firstCluster != 0)
                    {
                        fat_index = firstCluster;
                    }
                    else
                    {
                        fat_index = FAT.get_available_block();
                        fat_index = firstCluster;

                    }
                    List<byte[]> ls = new List<byte[]>();
                    for (int i = 0; i < num_full_Size; i++)
                    {
                        byte[] b = new byte[1024];
                        for (int j = 0; j < Directory_table_B.Length; i++)
                        {
                            b[j % 1024] = Directory_table_B[j];
                            if ((j + 1) % 1024 == 0)
                                ls.Add(b);
                        }

                    }
                    if (reminder > 0)
                    {
                        byte[] b = new byte[1024];
                        int start = num_full_Size * 1024;
                        for (int j = start; j < (start + reminder); j++)
                            b[j % 1024] = Directory_table_B[j];
                        ls.Add(b);


                    }

                    for (int i = 0; i < ls.Count; i++)
                    {
                        vertual_disk.write_block(ls[i], fat_index);
                        FAT.set_next(fat_index, -1);
                        if (fat_index != -1)
                            FAT.set_next(last_index, fat_index);
                        last_index = fat_index;
                        fat_index = FAT.get_available_block();
                    }
                    FAT.write_fat_table();

                }

            }
            public void read_Directory()
            {
                //  List<Directory_Entry> DE;
                List<byte> ls = new List<byte>();
                int fat_index = 0;
                int next;
                fat_index = firstCluster;
                next = FAT.get_next(fat_index);
                if (firstCluster != 0)
                {
                    do
                    {
                        ls.AddRange(vertual_disk.get_block(fat_index));
                        fat_index = next;
                        if (fat_index != -1)
                            next = FAT.get_next(fat_index);
                    } while (next != -1);

                }

            }
            public int search_Directory(string filename)
            {
                read_Directory();

                for (int i = 0; i < Directory_table.Count; i++)
                {
                    char[] f = filename.ToCharArray();
                    if (Directory_table[i].fileName == f)
                    {
                        return i;
                    }

                }
                return -1;

            }
            public void Update_Directory(Directory_Entry d)
            {
                read_Directory();
                string s = d.fileName.ToString();
                int index = search_Directory(s);
                if (index != -1)
                {
                    Directory_table.RemoveAt(index);
                    Directory_table.Insert(index, d);
                    write_Directory();
                }
            }
            public void Delete_Directory()
            {
                if (firstCluster != 0)
                {
                    int index = firstCluster;
                    int next = FAT.get_next(index);
                    do
                    {
                        FAT.set_next(index, 0);
                        if (index != -1)
                        {
                            index = next;
                            next = FAT.get_next(index);
                        }

                    } while (index != -1);
                    if (parent != null)
                    {
                        parent.read_Directory();
                        string s = fileName.ToString();
                        int I = parent.search_Directory(s);
                        if (I != -1)
                        {
                            parent.Directory_table.RemoveAt(I);
                            parent.write_Directory();
                            FAT.write_fat_table();
                        }
                    }
                }
            }
        }
        public class File_Entry : Directory_Entry
        {
            public Directory parent; public string content;
            public File_Entry(char[] fileName, byte fileAtterbute, int firstCluster, Directory parent) : base(fileName, fileAtterbute, firstCluster)
            {

                this.parent = parent;

                content = string.Empty;
            }



        }

        static void Main(string[] args)
        {
            string y;
            vertual_disk.initialize();

            var Getdir = Path.GetDirectoryName(System.Reflection.Assembly.GetExecutingAssembly().Location);


            while (true)
            {
                Console.Write(Getdir + ">> ");
                y = Console.ReadLine();

                command.check(y);




            }
        }
    }
}

