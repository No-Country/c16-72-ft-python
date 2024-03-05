
<div align=center >
    <img src="./project/static_dev/images/logos/logo_png.png" class="img-logo" alt="Centro médico Cousin" height=250 >
</div>
<hr>

<p>Este proyecto es un sistema de gestión de historias clínicas y estudios médicos para una clínica médica. Permite a los médicos administrar las historias clínicas y los estudios médicos de los pacientes, así como a los pacientes ver sus propios estudios e historias clínicas y descargar los estudios.</p>

<h2 align="center">
Puedes acceder a la aplicación web desplegada en: <br> <a href="https://miguelrizzi.pythonanywhere.com/">Centro médico Cousin</a>.
</h2>

<hr>

<h2 align="center">Equipo de Desarrollo</h2>

<table align="center">
  <tr>
    <td align="center">
      <img src="https://media.licdn.com/dms/image/D4D03AQHEUMBZW5Xwdg/profile-displayphoto-shrink_800_800/0/1695943376792?e=1715212800&v=beta&t=_d6iyef9wZ_ndapJIcveQV4iksKU3szGPqRNCx4ejJE" alt="Consuelo León Abarca" style="width: 150px; height: 150px;">
      <p><strong>Consuelo León Abarca</strong></p>
      <p>Diseñadora UX/UI</p>
      <a href="https://www.linkedin.com/in/consuelo-leon-abarca/">
        <img src="https://img.shields.io/badge/LinkedIn-%230077B5.svg?logo=linkedin&logoColor=white" alt="LinkedIn">
      </a> 
      <a href="https://github.com/consuelo0595">
        <img src="https://img.shields.io/badge/GitHub-%23181717.svg?logo=github&logoColor=white" alt="GitHub">
      </a>    
    </td>
    <td align="center">
      <img src="https://avatars.githubusercontent.com/u/151546685?v=4" alt="Sebastián Laverde" style="width: 150px; height: 150px;">
      <p><strong>Sebastián Laverde</strong></p>
      <p>Desarrollador Full Stack</p>
      <a href="https://www.linkedin.com/in/sebastian-laverde-51a33715b/"">
        <img src="https://img.shields.io/badge/LinkedIn-%230077B5.svg?logo=linkedin&logoColor=white" alt="LinkedIn">
      </a> 
      <a href="https://github.com/sbtn63">
        <img src="https://img.shields.io/badge/GitHub-%23181717.svg?logo=github&logoColor=white" alt="GitHub">
      </a>    
    </td>
    <td align="center">
      <img src="https://avatars.githubusercontent.com/u/89327840?v=4" alt="Brenda Huemer" style="width: 150px; height: 150px;">
      <p><strong>Brenda Huemer</strong></p>
      <p>Desarrolladora Full Stack</p>
      <a href="https://www.linkedin.com/in/brenda-huemer/">
        <img src="https://img.shields.io/badge/LinkedIn-%230077B5.svg?logo=linkedin&logoColor=white" alt="LinkedIn">
      </a> 
      <a href="https://github.com/brxndxz">
        <img src="https://img.shields.io/badge/GitHub-%23181717.svg?logo=github&logoColor=white" alt="GitHub">
      </a>    
    </td>
    <td align="center">
      <img src="https://media.licdn.com/dms/image/D4D03AQGj9Hcc9uny1Q/profile-displayphoto-shrink_800_800/0/1704305853538?e=1715212800&v=beta&t=QTiOgUX7qXPp4Lg2BYj0qURK35hB1DWsX2RwUJ4dO3Y" alt="Miguel Angel Rizzi" style="width: 150px; height: 150px;">
      <p><strong>Miguel Angel Rizzi</strong></p>
      <p>Desarrollador Full Stack</p>
      <a href="https://linkedin.com/in/miguel-angel-rizzi">
        <img src="https://img.shields.io/badge/LinkedIn-%230077B5.svg?logo=linkedin&logoColor=white" alt="LinkedIn">
      </a> 
      <a href="https://github.com/MiguelRizzi">
        <img src="https://img.shields.io/badge/GitHub-%23181717.svg?logo=github&logoColor=white" alt="GitHub">
      </a>
    </td>
  </tr>
</table>

<hr>

<h2>Funcionalidades principales</h2>
<ul>
        <li>Administración de Historias Clínicas: Los médicos pueden crear, ver, actualizar y eliminar historias clínicas de los pacientes.</li>
        <li>Administración de Estudios Médicos: Los médicos pueden cargar, ver, actualizar y eliminar estudios médicos de los pacientes.</li>
        <li>Acceso del Paciente: Los pacientes pueden ver sus propios estudios e historias clínicas, así como descargar los estudios.</li>
</ul>


<hr>

<h2>Tecnologías utilizadas</h2>
<ul>
  <li><img src="https://img.shields.io/badge/Python-%233776AB.svg?logo=python&logoColor=white" alt="Python"></li>
  <li><img src="https://img.shields.io/badge/Django-%23092E20.svg?logo=django&logoColor=white" alt="Django"></li>
  <li><img src="https://img.shields.io/badge/HTML/CSS-%23E34F26.svg?logo=html5&logoColor=white" alt="HTML/CSS"></li>
  <li><img src="https://img.shields.io/badge/JavaScript-%23F7DF1E.svg?logo=javascript&logoColor=black" alt="JavaScript"></li>
  <li><img src="https://img.shields.io/badge/jQuery-%230769AD.svg?logo=jquery&logoColor=white" alt="jQuery"></li>
</ul>

<hr>

<h2>Instalación y ejecución</h2>

<p>Pasos para instalar el proyecto:</p>

<ol>
    <li>Clone este repositorio en su máquina local usando el comando <code>git clone https://github.com/No-Country/c16-72-ft-python.git</code>.</li>
    <li>[Agrega los pasos específicos para instalar el entorno virtual y las dependencias]</li>
    <li>Para configurar las variables de entorno crea un archivo llamado <code>.env</code> en el directorio raíz de tu proyecto, a la altura del archivo <code>settings.py</code>. Dentro de este archivo, define las variables de entorno de la siguiente manera:<br>
    <pre>
        SECRET_KEY=tu_clave_secreta
        DEBUG=True
    </pre>
    </li>
    <li>Ejecute las migraciones de la base de datos usando los comandos <code>python manage.py makemigrations</code> y <code>python manage.py migrate</code>. Esto creará las tablas necesarias en la base de datos.</li>
    <li>Para ejecutar el servidor de desarrollo, muévase hasta el directorio del proyecto usando el comando <code>cd project</code> y use el comando <code>python manage.py runserver</code>. Esto iniciará el servidor en el puerto 8000 de su máquina local. Abre tu navegador y navega a <a href="http://localhost:8000">http://localhost:8000</a> para ver la aplicación en acción.</li>
    <li>Si quiere detener el servidor, simplemente presione <code>CTRL + C</code> en la consola donde está ejecutándose.</li>
</ol>

<hr>

<h2>Uso</h2>

<p>Una vez que el servidor esté en funcionamiento, puedes acceder al sistema a través de tu navegador web. Los médicos podrán iniciar sesión, administrar las historias clínicas y los estudios médicos, y los pacientes podrán iniciar sesión para ver y descargar sus propios estudios e historias clínicas.</p>

