<script>
(function(){
  var b=document.body;
  document.querySelectorAll('[data-menu]').forEach(function(btn){btn.addEventListener('click',function(){b.classList.toggle('menu-open');btn.setAttribute('aria-expanded',b.classList.contains('menu-open'));});});
  document.querySelectorAll('.nav-links a').forEach(function(a){a.addEventListener('click',function(){b.classList.remove('menu-open');});});
  document.querySelectorAll('form[data-join]').forEach(function(f){f.addEventListener('submit',function(e){e.preventDefault();var em=f.querySelector('input[type=email]');if(!em.value||!em.checkValidity()){em.reportValidity();em.focus();return;}f.innerHTML='<p class="thanks" role="status">Thank you. You are on the list, and you will hear from us soon.</p>';});});
  document.querySelectorAll('img').forEach(function(i){i.addEventListener('error',function(){var d=document.createElement('div');d.className=i.className+' img-fallback';d.setAttribute('role','img');d.setAttribute('aria-label',i.alt);i.replaceWith(d);});});
  if('IntersectionObserver' in window){var io=new IntersectionObserver(function(es){es.forEach(function(x){if(x.isIntersecting){x.target.classList.add('in');io.unobserve(x.target);}});},{threshold:.12});document.querySelectorAll('.reveal').forEach(function(el){io.observe(el);});}else{document.querySelectorAll('.reveal').forEach(function(el){el.classList.add('in');});}
  var y=document.getElementById('year');if(y)y.textContent=new Date().getFullYear();
})();
</script>
