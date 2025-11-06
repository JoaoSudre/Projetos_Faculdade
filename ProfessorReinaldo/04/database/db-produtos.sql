BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "produtos" (
	"idproduto"	INTEGER,
	"descricao"	TEXT,
	"precocompra"	REAL,
	"precovenda"	REAL,
	"datacriacao"	TEXT,
	PRIMARY KEY("idproduto" AUTOINCREMENT)
);
COMMIT;
