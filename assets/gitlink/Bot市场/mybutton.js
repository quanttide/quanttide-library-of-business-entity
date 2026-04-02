import React from 'react';  
import styles from './mybutton.module.css'; // 假设你有一个CSS模块文件来定义样式  
  
const MyButton = ({ onClick, children, className = '' }) => (  
  <button  
    onClick={onClick}  
    className={`${styles.myButton} ${className}`} // 使用CSS模块样式  
  >  
    {children}  
  </button>  
);  
  
export default MyButton;