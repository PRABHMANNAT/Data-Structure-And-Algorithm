/** Stable binary min-heap; equal priorities retain insertion order. */
export class MinHeap {
  constructor(){this.items=[];this.sequence=0;}
  get size(){return this.items.length;}
  less(a,b){return a.priority<b.priority || a.priority===b.priority&&a.order<b.order;}
  push(value,priority){
    const item={value,priority,order:this.sequence++};this.items.push(item);
    let index=this.items.length-1;
    while(index){const parent=(index-1)>>1;if(!this.less(item,this.items[parent]))break;this.items[index]=this.items[parent];index=parent;}
    this.items[index]=item;
  }
  pop(){
    if(!this.size)return null;
    const first=this.items[0],last=this.items.pop();
    if(this.size){let index=0;while(index*2+1<this.size){let child=index*2+1;if(child+1<this.size&&this.less(this.items[child+1],this.items[child]))child++;if(!this.less(this.items[child],last))break;this.items[index]=this.items[child];index=child;}this.items[index]=last;}
    return first.value;
  }
}
