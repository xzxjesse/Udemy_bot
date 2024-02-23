<?php
#buscar informações

$nome = "pedro";
$telefone = "123";

$sql = "SELECT * FROM bot WHERE nome = 'victor'";
$query = mysqli_query($conn, $sql);

while($rows_usuarios = mysqli_fetch_array($query)){
    $nome = $rows_usuarios['nome'];
    echo $nome;
}

?>