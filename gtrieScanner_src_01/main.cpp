/* -------------------------------------------------
      _       _     ___                            
 __ _| |_ _ _(_)___/ __| __ __ _ _ _  _ _  ___ _ _ 
/ _` |  _| '_| / -_)__ \/ _/ _` | ' \| ' \/ -_) '_|
\__, |\__|_| |_\___|___/\__\__,_|_||_|_||_\___|_|  
|___/                                          
    
gtrieScanner: quick discovery of network motifs
Released under Artistic License 2.0
(see README and LICENSE)

Pedro Ribeiro - CRACS & INESC-TEC, DCC/FCUP

----------------------------------------------------
Main File

Last Update: 11/02/2012
---------------------------------------------------- */

#include "CmdLine.h"

// "Global" Variables (acessible on every src file)
bool  Global::show_occ;
FILE *Global::occ_file;

// Main Function
int main(int argc, char **argv) {

  fprintf(stderr, "========== INICIANDO gtrieScanner ==========\n");
  fprintf(stderr, "Argumentos recibidos: %d\n", argc);
  for (int i = 0; i < argc; i++) {
    fprintf(stderr, "  argv[%d] = %s\n", i, argv[i]);
  }
  fflush(stderr);

  CmdLine::init(argc, argv);
  fprintf(stderr, "Inicialización completada\n");
  fflush(stderr);
  
  CmdLine::decide_action();
  fprintf(stderr, "Acción completada\n");
  fflush(stderr);
  
  CmdLine::finish();
  fprintf(stderr, "gtrieScanner finalizado correctamente\n");
  fflush(stderr);

  return 0;
}

