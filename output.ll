; ModuleID = "aprenda_modulo"
target triple = "unknown-unknown-unknown"
target datalayout = ""

declare i32 @"printf"(i8* %".1", ...)

declare i8* @"strcat"(i8* %".1", i8* %".2")

declare i8* @"strcpy"(i8* %".1", i8* %".2")

@"contador" = common global i32 0
define void @"saludar"(i8* %"nombre")
{
entry:
  %"nombre.1" = alloca i8*
  store i8* %"nombre", i8** %"nombre.1"
  %".4" = getelementptr inbounds [4 x i8], [4 x i8]* @"fstr0", i32 0, i32 0
  %".5" = getelementptr inbounds [7 x i8], [7 x i8]* @"str_1", i32 0, i32 0
  %"nombre.2" = load i8*, i8** %"nombre.1"
  %"buffer" = alloca [256 x i8]
  %"buffer_ptr" = bitcast [256 x i8]* %"buffer" to i8*
  %"strcpy_call" = call i8* @"strcpy"(i8* %"buffer_ptr", i8* %".5")
  %"strcat_call" = call i8* @"strcat"(i8* %"buffer_ptr", i8* %"nombre.2")
  %"printf_call" = call i32 (i8*, ...) @"printf"(i8* %".4", i8* %"buffer_ptr")
  ret void
}

@"fstr0" = private constant [4 x i8] c"%s\0a\00"
@"str_1" = private constant [7 x i8] c"Hola, \00"
define void @"main"()
{
entry:
  %".2" = getelementptr inbounds [6 x i8], [6 x i8]* @"str_2", i32 0, i32 0
  call void @"saludar"(i8* %".2")
  ret void
}

@"str_2" = private constant [6 x i8] c"Mundo\00"