#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define ARRAY "gbkuni30"
#define MAX_LEN 65535 // 2字节最大数
static unsigned short big_buffer[MAX_LEN] = {0};

// 源文件
#define SRC "gbkuni30.txt"

// 生产的头文件
#define DST "gbkuni30_gen.h"

int main()
{
    char buffer[16] = {0};
    char* p = NULL;
    FILE* fp_c = NULL;
    FILE* fp = NULL;
    int len = 0;
    int x1 = 0;
    int x2 = 0;
    int i = 0;
    int max_num = 0;
    int cnt = 0;

    fp = fopen(SRC, "r");
    if (fp == NULL)
    {
        printf("open file error!!\n");
        return -1;
    }

    fseek(fp, 0, SEEK_END);
    len = ftell(fp);
    fseek(fp,0,SEEK_SET);

    printf("file len: %d\n", len);

    fp_c = fopen(DST, "w+");
    if (fp_c == NULL)
    {
        printf("open file error!!\n");
        return -1;
    }

    fprintf(fp_c, "/**********************************************************************************/\n");
    fprintf(fp_c, "/* GBK(GB18030) to UNICODE table, powered by Late Lee */\n");
    fprintf(fp_c, "/* http://www.latelee.org */\n");
    fprintf(fp_c, "/* %s %s */\n", __DATE__, __TIME__);
    fprintf(fp_c, "/* The source file comes from: */\n");
    fprintf(fp_c, "/* http://icu-project.org/repos/icu/data/trunk/charset/source/gb18030/gbkuni30.txt*/\n");

    fprintf(fp_c, "/**********************************************************************************/\n");

    fprintf(fp_c, "#ifndef __GBK2UNICODE__H\n");
    fprintf(fp_c, "#define __GBK2UNICODE__H\n\n");

    fprintf(fp_c, "static unsigned short %s[] = \n{\n", ARRAY);

    // 先读取到缓冲区，解析出两个数
    while (fgets(buffer, 32, fp) != NULL)
    {
        sscanf(buffer, "%x:%x\n", &x1, &x2);

        //printf("%s", buffer);
        //printf("%04x %x\n", x2, x1);
        //fprintf(fp_c, "0x%04x, 0x%x,\n", x1, x2);
        big_buffer[x2] = x1;
        if (x2 > max_num)
            max_num = x2;
    }

    printf("max num: %d %x\n", max_num, max_num);
    // 注：为节省存储空间，从0x8140开始存储，查询时需要减去此数
    for (i = 0x8140; i < max_num + 1; i++) // 0x8140
    {
        //printf("%x --> 0x%04x\n", i, big_buffer[i]);
        fprintf(fp_c, "0x%04x, ", big_buffer[i]);
        cnt++;
        if (cnt % 10 == 0)
        {
            fprintf(fp_c, " // line num %d \n", cnt / 10 - 1);
        }
    }
    fprintf(fp_c, "\n");
    fprintf(fp_c, "};\n\n");
    fprintf(fp_c, "#endif //__GBK2UNICODE__H\n");
    fprintf(stdout, "Job done!\n");

    fclose(fp);
    fclose(fp_c);

    return 0;
}