void setup () {
  size(500, 500);
}

void draw(){
   float r = 0.45*width;
   float rPontSegundos = r * 0.98;
   float rPontMinutos = r * 0.95;
   float rPontHoras = r * 0.92;
   float rSegundos = r * 0.90;
   float rMinutos = r * 0.70;
   float rHoras = r * 0.50;
   float anguloSegundos = (second()*(PI/30)) - (PI/2);
   float anguloMinutos = (((minute()*60) + second())* (PI/1800)) - (PI/2);
   //float anguloHoras = (((hour()*3600) + ((minute() * 60) + second())) * (PI/108000)) - (PI/2);
   float anguloHoras = (((hour()*3600) + ((minute() * 60) + second())) * (PI/21600)) - (PI/2);
   translate(width/2, height/2);
   
   background(255,255,255);
   
   beginShape();
     ellipse(0,0,2*r,2*r);
     strokeWeight(3);
     fill(0,0,0);
     ellipse(0,0,10,10);
     noFill();
     strokeWeight(1);
     
     stroke(255,0,0);
     line(0,0,rSegundos*cos(TWO_PI+anguloSegundos),rSegundos*sin(TWO_PI+anguloSegundos));
     stroke(0);
     strokeWeight(2);
     line(0,0,rMinutos*cos(TWO_PI+anguloMinutos),rMinutos*sin(TWO_PI+anguloMinutos));
     strokeWeight(1);
     strokeWeight(3);
     line(0,0,rHoras*cos(TWO_PI+anguloHoras),rHoras*sin(TWO_PI+anguloHoras));
     strokeWeight(1);
     
     //int hora = 
     
     for(int angulo = 0; angulo <= 360 ;angulo++){
       float anguloRadSegundos = angulo * (PI/150);
       float anguloRadMinutos = angulo * (PI/30);
       float anguloRadHoras = (angulo * (PI/6)) - (PI/2);
       
       //fill(0,0,0);
       //text("gfadsadasdas",rPontHoras*cos(anguloRadHoras), rPontHoras*sin(anguloRadHoras));
       //noFill();
       line(rPontSegundos*cos(anguloRadSegundos), rPontSegundos*sin(anguloRadSegundos),r*cos(anguloRadSegundos),r*sin(anguloRadSegundos));
       line(rPontMinutos*cos(anguloRadMinutos), rPontMinutos*sin(anguloRadMinutos),r*cos(anguloRadMinutos),r*sin(anguloRadMinutos));
       strokeWeight(3);
       line(rPontHoras*cos(anguloRadHoras), rPontHoras*sin(anguloRadHoras),r*cos(anguloRadHoras),r*sin(anguloRadHoras)); 
       strokeWeight(1);
     }
    endShape(CLOSE); 
    
}
