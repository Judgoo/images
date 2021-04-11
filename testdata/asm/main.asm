section .data
    msg db "helloworld", 0ah

section .text
    global _start
_start:
    mov rax, 1
    mov rdi, 1
    mov rsi, msg
    mov rdx, 10
    syscall
    mov rax, 60
    mov rdi, 0
    syscall
