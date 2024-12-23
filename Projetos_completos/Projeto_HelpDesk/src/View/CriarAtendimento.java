/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/GUIForms/JDialog.java to edit this template
 */
package View;

import Model.Atendimento;
import Controller.AtendimentoDAO;
import Controller.ClienteDAO;
import Controller.SetorDAO;
import java.sql.SQLException;
import java.util.logging.Level;
import java.util.logging.Logger;

/**
 *
 * @author guilherme
 */
public class CriarAtendimento extends javax.swing.JDialog {

    private static int idCliente;
    
    public CriarAtendimento(int idCliente) throws SQLException{
        initComponents();
        this.erro.setVisible(false);
        this.idCliente = idCliente;
        AtendimentoDAO ad = new AtendimentoDAO();
        SetorDAO sd = new SetorDAO();
    }

    /**
     * This method is called from within the constructor to initialize the form.
     * WARNING: Do NOT modify this code. The content of this method is always
     * regenerated by the Form Editor.
     */
    @SuppressWarnings("unchecked")
    // <editor-fold defaultstate="collapsed" desc="Generated Code">//GEN-BEGIN:initComponents
    private void initComponents() {

        buttonGroup1 = new javax.swing.ButtonGroup();
        jLabel1 = new javax.swing.JLabel();
        jLabel2 = new javax.swing.JLabel();
        cadastroTipo = new javax.swing.JTextField();
        jLabel3 = new javax.swing.JLabel();
        cadastroIdEquipamento = new javax.swing.JTextField();
        jLabel4 = new javax.swing.JLabel();
        cadastroUrgencia = new javax.swing.JComboBox<>();
        jScrollPane1 = new javax.swing.JScrollPane();
        cadastroDescricao = new javax.swing.JTextArea();
        jLabel5 = new javax.swing.JLabel();
        jLabel6 = new javax.swing.JLabel();
        cadastroSetor = new javax.swing.JComboBox<>();
        cadastrarAtendimento = new javax.swing.JButton();
        limpar = new javax.swing.JButton();
        cancelar = new javax.swing.JButton();
        erro = new javax.swing.JLabel();

        setDefaultCloseOperation(javax.swing.WindowConstants.DISPOSE_ON_CLOSE);

        jLabel1.setFont(new java.awt.Font("Segoe UI", 1, 48)); // NOI18N
        jLabel1.setText("Cadastrar chamado");

        jLabel2.setFont(new java.awt.Font("Segoe UI", 0, 24)); // NOI18N
        jLabel2.setText("Tipo de equipamento");

        cadastroTipo.setFont(new java.awt.Font("Segoe UI", 0, 18)); // NOI18N
        cadastroTipo.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                cadastroTipoActionPerformed(evt);
            }
        });

        jLabel3.setFont(new java.awt.Font("Segoe UI", 0, 24)); // NOI18N
        jLabel3.setText("Id do equipamento");

        cadastroIdEquipamento.setFont(new java.awt.Font("Segoe UI", 0, 18)); // NOI18N
        cadastroIdEquipamento.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                cadastroIdEquipamentoActionPerformed(evt);
            }
        });

        jLabel4.setFont(new java.awt.Font("Segoe UI", 0, 24)); // NOI18N
        jLabel4.setText("Tipo de urgência");

        cadastroUrgencia.setFont(new java.awt.Font("Segoe UI", 0, 24)); // NOI18N
        cadastroUrgencia.setModel(new javax.swing.DefaultComboBoxModel<>(new String[] { "Sem urgência", "Urgente!" }));

        cadastroDescricao.setColumns(20);
        cadastroDescricao.setFont(new java.awt.Font("Segoe UI", 0, 20)); // NOI18N
        cadastroDescricao.setLineWrap(true);
        cadastroDescricao.setRows(5);
        jScrollPane1.setViewportView(cadastroDescricao);

        jLabel5.setFont(new java.awt.Font("Segoe UI", 0, 24)); // NOI18N
        jLabel5.setText("Descrição do problema");

        jLabel6.setFont(new java.awt.Font("Segoe UI", 0, 24)); // NOI18N
        jLabel6.setText("Setor onde se encontra");

        cadastroSetor.setFont(new java.awt.Font("Segoe UI", 0, 24)); // NOI18N
        cadastroSetor.setModel(new javax.swing.DefaultComboBoxModel<>(new String[] { "TI", "Admin", "RH", "Manutenção", "Segurança", "Comercial" }));

        cadastrarAtendimento.setFont(new java.awt.Font("Segoe UI", 0, 24)); // NOI18N
        cadastrarAtendimento.setText("Enviar!");
        cadastrarAtendimento.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                cadastrarAtendimentoActionPerformed(evt);
            }
        });

        limpar.setFont(new java.awt.Font("Segoe UI", 0, 24)); // NOI18N
        limpar.setText("Limpar");
        limpar.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                limparActionPerformed(evt);
            }
        });

        cancelar.setFont(new java.awt.Font("Segoe UI", 0, 24)); // NOI18N
        cancelar.setText("Cancelar");
        cancelar.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                cancelarActionPerformed(evt);
            }
        });

        erro.setFont(new java.awt.Font("Segoe UI", 0, 24)); // NOI18N
        erro.setForeground(new java.awt.Color(255, 0, 0));
        erro.setText("Erro ao cadastrar um chamado!");

        javax.swing.GroupLayout layout = new javax.swing.GroupLayout(getContentPane());
        getContentPane().setLayout(layout);
        layout.setHorizontalGroup(
            layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(layout.createSequentialGroup()
                .addGap(42, 42, 42)
                .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                    .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING, false)
                        .addComponent(jLabel2, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE)
                        .addComponent(cadastroTipo))
                    .addComponent(cadastroIdEquipamento, javax.swing.GroupLayout.PREFERRED_SIZE, 231, javax.swing.GroupLayout.PREFERRED_SIZE)
                    .addGroup(layout.createSequentialGroup()
                        .addGap(16, 16, 16)
                        .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                            .addComponent(jLabel3)
                            .addGroup(layout.createSequentialGroup()
                                .addGap(12, 12, 12)
                                .addComponent(jLabel4))))
                    .addComponent(cadastroUrgencia, javax.swing.GroupLayout.PREFERRED_SIZE, 231, javax.swing.GroupLayout.PREFERRED_SIZE))
                .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                    .addGroup(layout.createSequentialGroup()
                        .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED, javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE)
                        .addComponent(jLabel5, javax.swing.GroupLayout.PREFERRED_SIZE, 261, javax.swing.GroupLayout.PREFERRED_SIZE)
                        .addContainerGap(javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE))
                    .addGroup(layout.createSequentialGroup()
                        .addGap(71, 71, 71)
                        .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.TRAILING)
                            .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                                .addComponent(jLabel1)
                                .addGroup(layout.createSequentialGroup()
                                    .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                                        .addComponent(jLabel6)
                                        .addGroup(layout.createSequentialGroup()
                                            .addGap(10, 10, 10)
                                            .addComponent(cadastroSetor, javax.swing.GroupLayout.PREFERRED_SIZE, 231, javax.swing.GroupLayout.PREFERRED_SIZE)))
                                    .addGap(92, 92, 92)
                                    .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.TRAILING, false)
                                        .addComponent(cadastrarAtendimento, javax.swing.GroupLayout.PREFERRED_SIZE, 309, javax.swing.GroupLayout.PREFERRED_SIZE)
                                        .addGroup(layout.createSequentialGroup()
                                            .addComponent(limpar, javax.swing.GroupLayout.PREFERRED_SIZE, 140, javax.swing.GroupLayout.PREFERRED_SIZE)
                                            .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED, javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE)
                                            .addComponent(cancelar, javax.swing.GroupLayout.PREFERRED_SIZE, 142, javax.swing.GroupLayout.PREFERRED_SIZE)))))
                            .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                                .addComponent(erro)
                                .addComponent(jScrollPane1, javax.swing.GroupLayout.PREFERRED_SIZE, 603, javax.swing.GroupLayout.PREFERRED_SIZE)))
                        .addGap(114, 114, 114))))
        );
        layout.setVerticalGroup(
            layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(layout.createSequentialGroup()
                .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                    .addGroup(layout.createSequentialGroup()
                        .addContainerGap()
                        .addComponent(jLabel1)
                        .addGap(21, 21, 21)
                        .addComponent(erro)
                        .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.UNRELATED)
                        .addComponent(jLabel5)
                        .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                        .addComponent(jScrollPane1, javax.swing.GroupLayout.PREFERRED_SIZE, 202, javax.swing.GroupLayout.PREFERRED_SIZE))
                    .addGroup(layout.createSequentialGroup()
                        .addGap(143, 143, 143)
                        .addComponent(jLabel2)
                        .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.UNRELATED)
                        .addComponent(cadastroTipo, javax.swing.GroupLayout.PREFERRED_SIZE, 52, javax.swing.GroupLayout.PREFERRED_SIZE)
                        .addGap(67, 67, 67)
                        .addComponent(jLabel3)
                        .addGap(24, 24, 24)
                        .addComponent(cadastroIdEquipamento, javax.swing.GroupLayout.PREFERRED_SIZE, 52, javax.swing.GroupLayout.PREFERRED_SIZE)))
                .addGap(50, 50, 50)
                .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE)
                    .addComponent(jLabel4)
                    .addComponent(jLabel6)
                    .addComponent(cadastrarAtendimento))
                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE)
                    .addComponent(cadastroSetor, javax.swing.GroupLayout.PREFERRED_SIZE, 52, javax.swing.GroupLayout.PREFERRED_SIZE)
                    .addComponent(cadastroUrgencia, javax.swing.GroupLayout.PREFERRED_SIZE, 52, javax.swing.GroupLayout.PREFERRED_SIZE)
                    .addComponent(limpar)
                    .addComponent(cancelar))
                .addGap(52, 52, 52))
        );

        pack();
    }// </editor-fold>//GEN-END:initComponents

    private void cadastroTipoActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_cadastroTipoActionPerformed
        // TODO add your handling code here:
    }//GEN-LAST:event_cadastroTipoActionPerformed

    private void cadastroIdEquipamentoActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_cadastroIdEquipamentoActionPerformed
        // TODO add your handling code here:
    }//GEN-LAST:event_cadastroIdEquipamentoActionPerformed

    private void cadastrarAtendimentoActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_cadastrarAtendimentoActionPerformed
        int r = 0;
        AtendimentoDAO ad = new AtendimentoDAO();
        Atendimento atendimento = new Atendimento();
        
        atendimento.setTipoEquipamento(this.cadastroTipo.getText());
        atendimento.setIdEquipamento(this.cadastroIdEquipamento.getText());
        atendimento.setDescricao(this.cadastroDescricao.getText());
        atendimento.setUrgencia(this.cadastroUrgencia.getSelectedIndex());
        
        SetorDAO sd = new SetorDAO();
        try {
            int i = this.cadastroSetor.getSelectedIndex()+1;
            atendimento.setSetorAtendimento(sd.buscaSetor(i));
        } catch (SQLException ex) {
            Logger.getLogger(CriarAtendimento.class.getName()).log(Level.SEVERE, null, ex);
        }
        
        atendimento.setStatus(0);
        System.out.println(atendimento);
        
        r = ad.inserirAtendimento(atendimento);
        
        if(r>0){
            this.dispose();
            try {
                new TelaCliente(this.idCliente).setVisible(true);
            } catch (SQLException ex) {
                Logger.getLogger(CriarAtendimento.class.getName()).log(Level.SEVERE, null, ex);
            }
        }
        else
            this.erro.setVisible(true);
    }//GEN-LAST:event_cadastrarAtendimentoActionPerformed

    private void limparActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_limparActionPerformed
        this.erro.setVisible(false);
        this.cadastroTipo.setText("");
        this.cadastroIdEquipamento.setText("");
        this.cadastroDescricao.setText("");
    }//GEN-LAST:event_limparActionPerformed

    private void cancelarActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_cancelarActionPerformed
       this.dispose();
        try {
            new TelaCliente(this.idCliente).setVisible(true);
        } catch (SQLException ex) {
            Logger.getLogger(CriarAtendimento.class.getName()).log(Level.SEVERE, null, ex);
        }
    }//GEN-LAST:event_cancelarActionPerformed

    /**
     * @param args the command line arguments
     */
    public static void main(String args[]) {
        /* Set the Nimbus look and feel */
        //<editor-fold defaultstate="collapsed" desc=" Look and feel setting code (optional) ">
        /* If Nimbus (introduced in Java SE 6) is not available, stay with the default look and feel.
         * For details see http://download.oracle.com/javase/tutorial/uiswing/lookandfeel/plaf.html 
         */
        try {
            for (javax.swing.UIManager.LookAndFeelInfo info : javax.swing.UIManager.getInstalledLookAndFeels()) {
                if ("Nimbus".equals(info.getName())) {
                    javax.swing.UIManager.setLookAndFeel(info.getClassName());
                    break;
                }
            }
        } catch (ClassNotFoundException ex) {
            java.util.logging.Logger.getLogger(CriarAtendimento.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        } catch (InstantiationException ex) {
            java.util.logging.Logger.getLogger(CriarAtendimento.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        } catch (IllegalAccessException ex) {
            java.util.logging.Logger.getLogger(CriarAtendimento.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        } catch (javax.swing.UnsupportedLookAndFeelException ex) {
            java.util.logging.Logger.getLogger(CriarAtendimento.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        }
        //</editor-fold>

        /* Create and display the dialog */
        java.awt.EventQueue.invokeLater(new Runnable() {
            public void run() {
                CriarAtendimento dialog = null;
                try {
                    dialog = new CriarAtendimento(idCliente);
                } catch (SQLException ex) {
                    Logger.getLogger(CriarAtendimento.class.getName()).log(Level.SEVERE, null, ex);
                }
                dialog.addWindowListener(new java.awt.event.WindowAdapter() {
                    @Override
                    public void windowClosing(java.awt.event.WindowEvent e) {
                        System.exit(0);
                    }
                });
                dialog.setVisible(true);
            }
        });
    }

    // Variables declaration - do not modify//GEN-BEGIN:variables
    private javax.swing.ButtonGroup buttonGroup1;
    private javax.swing.JButton cadastrarAtendimento;
    private javax.swing.JTextArea cadastroDescricao;
    private javax.swing.JTextField cadastroIdEquipamento;
    private javax.swing.JComboBox<String> cadastroSetor;
    private javax.swing.JTextField cadastroTipo;
    private javax.swing.JComboBox<String> cadastroUrgencia;
    private javax.swing.JButton cancelar;
    private javax.swing.JLabel erro;
    private javax.swing.JLabel jLabel1;
    private javax.swing.JLabel jLabel2;
    private javax.swing.JLabel jLabel3;
    private javax.swing.JLabel jLabel4;
    private javax.swing.JLabel jLabel5;
    private javax.swing.JLabel jLabel6;
    private javax.swing.JScrollPane jScrollPane1;
    private javax.swing.JButton limpar;
    // End of variables declaration//GEN-END:variables
}
