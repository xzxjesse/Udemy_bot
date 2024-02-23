<?php
#atualizar informações

$nome = "pedro";
$telefone = "123";

$sql = "UPDATE bot SET nome = '$nome' WHERE id=1";
$query = mysqli_query($conn, $sql);

if(!$query){
    echo "erro ao atualizar";
} else{
    echo "atualizada com sucesso";
}
?>