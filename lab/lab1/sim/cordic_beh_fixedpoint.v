`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 06.03.2023 19:09:11
// Design Name: 
// Module Name: cordic_beh_fixedpoint
// Project Name: 
// Target Devices: 
// Tool Versions: 
// Description: 
// 
// Dependencies: 
// 
// Revision:
// Revision 0.01 - File Created
// Additional Comments:
// 
//////////////////////////////////////////////////////////////////////////////////

//Exercise 2.1
//Write the cordic algorithm using the signed fixed-point [12:10] data representation. Use
//arithmetic shift right for the division operation. Simulate the resulting code in Verilog
//simulator


module cordic_beh_fixedpoint();


parameter integer FXP_SCALE = 1024;
reg signed [11:0] t_angle = 0.8 * FXP_SCALE; //Input angle
reg signed [11:0] cos = 1.0 * FXP_SCALE; //Initial condition
reg signed [11:0] sin = 0.0;
reg signed [11:0] angle = 0.0; //Running angle
reg signed [11:0] atan[0:10] = {804,475,251,127,64,32,16,8,4,2,1}; // jak cos tto to w exelu jest 
reg signed [11:0] Kn = 0.607253 * FXP_SCALE;

reg signed [23:0] sin_res = 0.0;
reg signed [23:0] cos_res = 0.0;

real cos_output = 1.0; //Initial vector x coordinate
real sin_output = 0.0; //and y coordinate

integer i, d;
//real tmp;
reg signed [23:0] tmp = 0; 
initial //Execute only once
begin
 for ( i = 0; i < 11; i = i + 1) //Ten algorithm iterations
 begin
 # 10
 if( t_angle > angle )
 begin
 angle = ( angle + atan[i]) >> 0; // bo [m+1|n] 
 tmp = cos - ( sin >> i );
 sin = (( cos >> i ) + sin) >> 0;
 cos = tmp;
 end
 else
 begin
 angle = angle - atan[i];
 tmp = (cos + ( sin >> i )) >> 0;
 sin = (- ( cos >> i) + sin) >> 0;
 cos = tmp;
 end //if
 end //for
 //Scale sin/cos values
 sin_res = (Kn * sin) >> 10;
 cos_res = (Kn * cos) >> 10;
 
 cos_output = $itor(cos_res) / FXP_SCALE;
 sin_output = $itor(sin_res) / FXP_SCALE;
 
 $display("sin=%f, cos=%f", sin_output , cos_output );
end

endmodule
