import java.util.*;

class Footwear
{
    public Footwear(int footwearId,String brandName,String footwearType,int price){
        this.footwearId = footwearId;
        this.brandName = brandName;
        this.footwearType = footwearType;
        this.price = price;
    }
    public int getFootwearId() {
        return footwearId;
    }
    public void setFootwearId(int footwearId) {
        this.footwearId = footwearId;
    }
    public String getBrandName() {
        return brandName;
    }
    public void setBrandName(String brandName) {
        this.brandName = brandName;
    }
    public String getFootwearType() {
        return footwearType;
    }
    public void setFootwearType(String footwearType) {
        this.footwearType = footwearType;
    }
    public int getPrice() {
        return price;
    }
    public void setPrice(int price) {
        this.price = price;
    }
    private int footwearId;
    private String brandName;
    private String footwearType;
    private int price;
}

class SortByPrice implements Comparator<Footwear>
{
    public int compare(Footwear a, Footwear b)
    {
        return a.getPrice() - b.getPrice();
}
}

class Solution { 
    public static void main(String args[]){
        Footwear demo = new Footwear(16, "relaxo", "loafer", 12);
        Footwear demo2 = new Footwear(16, "relaxo", "loafer", 11);
        Footwear demo3 = new Footwear(16, "relaxo", "loafer", 26);
        Footwear arrayOfFootwear[] = new Footwear[3];
        arrayOfFootwear[0] = demo;
        arrayOfFootwear[1] = demo2;
        arrayOfFootwear[2] = demo3;
        String footwear_type = "loafer";
        String brandname = "relaxo";
        int count = getCountByType(arrayOfFootwear, footwear_type);
        String to_print = "Footwear not available";
        if (count > 0){
            to_print = count+"";
        }
        System.out.println(to_print);
        Footwear second_high = getSecondHighestPriceByBrand(arrayOfFootwear, brandname);
        if (second_high !=null){
            System.out.println(second_high.getFootwearId());
            System.out.println(second_high.getFootwearType());
            System.out.println(second_high.getPrice());
        }else{
            System.out.println("Brand not available");
        }
    }
    public static int getCountByType(Footwear[] arrayOfFootwear, String footweartype){
        int count = 0;
        for (int arrayindex =0;arrayindex < arrayOfFootwear.length; arrayindex++)
        {
            if(arrayOfFootwear[arrayindex].getFootwearType().equals(footweartype)){
                count++;
            }
        }
        return count;
    }
    public static Footwear getSecondHighestPriceByBrand(Footwear[] arrayOfFootwear, String footwear){
        ArrayList<Footwear> arr = new ArrayList<>();
        for(int i =0; i < arrayOfFootwear.length; i++){
            if (arrayOfFootwear[i].getBrandName().equals(footwear)){
                arr.add((Footwear)arrayOfFootwear[i]);
            }
        }        
        Collections.sort(arr, new SortByPrice());
        if(arr.size()==0){
            return null;
        }
        Footwear second_highest = arr.get(arr.size()-2);
        return second_highest;
    }   
}