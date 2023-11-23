#include<stdio.h>
#include <unistd.h>

__attribute__((constructor)) void setup(){
	setbuf(stdin, NULL);
	setbuf(stdout, NULL);
	setbuf(stderr, NULL);
}

void useful() {
    __asm__("pop %rdi;ret;");
    __asm__("pop %rsi;ret;");
    __asm__("pop %rdx;ret;");
    __asm__("pop %rcx;ret;");
    __asm__("pop %r8;ret;");
    __asm__("pop %r9;ret;");
}

void save_beteg(int goat, int wolf , int hunter, int mouse, int boy , int parent){
    if (goat != 0xdeadface){
        printf("Чиний хатсан харганыг идэх байтугай, шимтэй ногоогоо идэж барахгүй яая гэж байна» гээд тоосонгүй гэнэ. Тэгэхлээр нь Бэтгэлжин бор шувуу");
        return;
    }
    if (wolf != 0xdeadbeef){
        printf("Чиний туранхай ямааг идэх нь байтугай тураг гөрөөсөө яаж идэх билээ гэж явна");
        return;
    }
    if (hunter != 0xabcdef01){
        printf("Гуриатсан чоно хөөцөлдөх нь байтугай, гуу жалгын гөрөөсөө намнаж чадахгүй явна");
        return;
    }
    if (mouse !=0xbaadf00d){
        printf("Гөрөөчний дээл ноохойлох нь байтугай хөеөгөө яаж хураая гэж ядаж явна» гээд тоосонгүй гэнэ");
        return;
    }
    if (boy!=0xfeedface){
        printf("Хулгана зурамтай хөөцөлдөх нь байтугай, хурга ишгээ хариулж гүйцэхгүй яая гэж явна");
        return;
    }
    if (parent!=0xcafebabe){
        printf("Тархигүй хүүхэдтэй хөөцөлдөх нь байтугай, тараасан унгасаа савж амжихгүй яая ийя гэж байна");
        return;
    }

    system("/bin/sh");
}

int vuln(){
    char buffer[0x10];
    puts("Эрт урьд цагт нар сая мандаж, навч сая дэлгэрч, төр сая тогтож, түмэн сая хурж байхад Бэтгэтэй бор шувуу гэж байж гэнэ. Тэр шувуу өвлийн хүйтэнд өлсөнө гэж, хаврын хатууд харшана гэж хайртай бэтгэ гүзээндээ чимх будаа чихэж, атга будаа агуулсан юм байжээ. Тэгээд нэг өдөр тэнгэрт нисч ядраад харгана сондуул дээр суутал хайртай бэтгийг нь хагалчих гээд хатгаад байж гэнэ. ");
    gets(buffer);
    return 0;
}

int main(){
    vuln();
    printf("Бэтгээ хамгаалж чадсангүй!");
}