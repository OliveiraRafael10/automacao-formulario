// Aguarda o carregamento completo do DOM antes de executar os scripts
document.addEventListener('DOMContentLoaded', function() {
    
    /**
     * Gerenciamento do envio do formulário
     * Previne o envio real e exibe mensagem de sucesso
     */
    const formulario = document.getElementById('formularioCadastro');
    const senha = document.getElementById('senha');
    const confirmarSenha = document.getElementById('confirmarSenha');
    
    formulario.addEventListener('submit', function(e) {
        // Previne o comportamento padrão de envio do formulário
        e.preventDefault();
        
        // Valida se as senhas são iguais
        if (senha.value !== confirmarSenha.value) {
            alert('As senhas não coincidem! Por favor, verifique.');
            confirmarSenha.focus();
            confirmarSenha.style.borderColor = '#f44336';
            return;
        }
        
        // Exibe a mensagem de sucesso
        const mensagem = document.getElementById('mensagemSucesso');
        mensagem.classList.add('mostrar');
        
        // Oculta a mensagem após 3 segundos e limpa o formulário
        setTimeout(() => {
            mensagem.classList.remove('mostrar');
            // Reseta todos os campos do formulário
            formulario.reset();
            // Remove as cores de validação dos campos
            resetarCoresValidacao();
        }, 3000);
    });

    /**
     * Máscara de telefone (00) 00000-0000
     */
    const telefone = document.getElementById('telefone');
    
    telefone.addEventListener('input', function(e) {
        let value = e.target.value.replace(/\D/g, ''); // Remove tudo que não é dígito
        
        if (value.length > 11) {
            value = value.slice(0, 11);
        }
        
        // Aplica a máscara
        if (value.length > 10) {
            value = value.replace(/^(\d{2})(\d{5})(\d{4}).*/, '($1) $2-$3');
        } else if (value.length > 6) {
            value = value.replace(/^(\d{2})(\d{4})(\d{0,4}).*/, '($1) $2-$3');
        } else if (value.length > 2) {
            value = value.replace(/^(\d{2})(\d{0,5})/, '($1) $2');
        } else if (value.length > 0) {
            value = value.replace(/^(\d*)/, '($1');
        }
        
        e.target.value = value;
    });

    /**
     * Validação em tempo real da confirmação de senha
     */
    confirmarSenha.addEventListener('input', function() {
        if (this.value === '') {
            this.style.borderColor = '#e0e0e0';
        } else if (this.value === senha.value) {
            this.style.borderColor = '#4caf50';
        } else {
            this.style.borderColor = '#f44336';
        }
    });

    senha.addEventListener('input', function() {
        if (confirmarSenha.value !== '' && confirmarSenha.value === this.value) {
            confirmarSenha.style.borderColor = '#4caf50';
        } else if (confirmarSenha.value !== '') {
            confirmarSenha.style.borderColor = '#f44336';
        }
    });

    /**
     * Validação em tempo real dos campos
     * Adiciona feedback visual quando o usuário sai do campo (evento blur)
     */
    const inputs = document.querySelectorAll('input');
    
    inputs.forEach(input => {
        // Evento disparado quando o campo perde o foco
        input.addEventListener('blur', function() {
            if (this.validity.valid) {
                // Campo válido - borda verde
                this.style.borderColor = '#4caf50';
            } else if (this.value !== '') {
                // Campo inválido com conteúdo - borda vermelha
                this.style.borderColor = '#f44336';
            }
        });

        // Evento disparado durante a digitação
        input.addEventListener('input', function() {
            // Se o campo estiver vazio, volta para a cor padrão
            if (this.value === '') {
                this.style.borderColor = '#e0e0e0';
            }
        });
    });

    /**
     * Função auxiliar para resetar as cores de validação dos campos
     * Usada após o reset do formulário
     */
    function resetarCoresValidacao() {
        inputs.forEach(input => {
            input.style.borderColor = '#e0e0e0';
        });
    }
});

