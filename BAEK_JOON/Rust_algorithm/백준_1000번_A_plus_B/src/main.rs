use std::io;
fn main() {
    let mut s = String::new();
    io::stdin().read_line(&mut s)
        .expect("error");
    
    /*let a = s[..1].to_string();
    let b = s[2..3].to_string();

    let a: u32 = a.parse()
        .expect("error");
    let b: u32 = b.parse()
        .expect("error");
    println!("{}",a + b);
    */

    //-----------------------
    let b = &s.as_bytes();
    println!("{}",b[0] + b[2] - 2*b'0');
}
