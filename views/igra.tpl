% import model
<!DOCTYPE html>
<html>

<body>

  <h1>Vislice</h1>

  <blockquote>
    Vislice so najboljša igra za preganjanje dolgčasa (poleg tetrisa).
    <small>Študentje</small>
  </blockquote>
  
  <h2> {{ igra.pravilni_del_gesla() }}  </h2>

  <h2> napacna_ugibanja </h2>

% if poskus == model.ZMAGA:
 <h1> ZMAGAL SI </h2>
% elif poskus == model.PORAZ:
 <h1> IZGUBIL SI </h2>
% else:


  <img src="img/10.jpg" alt="obesanje">

  <form action="/igra/{{id_igre}}" method="post">
  Črka: <input type="text" name="crka">
    <button type="submit">Ugibaj</button>
  </form>
</body>

</html>